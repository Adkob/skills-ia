---
name: createur-de-competences
description: Crée de nouvelles compétences, modifie et améliore des compétences existantes, et mesure leurs performances. À utiliser systématiquement dès qu'il s'agit de concevoir, rédiger, corriger ou améliorer une compétence (skill) — que la demande soit "crée une compétence pour...", "transforme ce workflow en skill", "améliore cette compétence", "lance des évaluations (evals)", ou pour optimiser le déclenchement (triggering) d'une compétence existante. À utiliser même si l'utilisateur ne prononce pas explicitement le mot "compétence" ou "skill".
---

# Créateur de compétences

Une compétence pour créer de nouvelles compétences (skills) et les améliorer de manière itérative.

À un niveau macro, le processus de création d'une compétence se déroule ainsi :
- Décider de ce que la compétence doit faire et comment.
- Rédiger un brouillon de la compétence (SKILL.md).
- Créer quelques invites (prompts) de test et lancer des agents avec accès à la compétence sur ces tests.
- Aider l'utilisateur à évaluer les résultats de manière qualitative et quantitative.
  - Pendant que les tests s'exécutent en arrière-plan, rédiger des évaluations quantitatives (assertions) s'il n'y en a pas, et les expliquer à l'utilisateur.
  - Utiliser le script `eval-viewer/generate_review.py` pour montrer les résultats à l'utilisateur afin qu'il les examine, ainsi que les métriques quantitatives.
- Réécrire la compétence en fonction des retours de l'évaluation et des éventuels défauts flagrants mis en évidence par les benchmarks.
- Répéter jusqu'à satisfaction.
- (Optionnel) Optimiser la description de la compétence.

Votre rôle lorsque vous utilisez cette compétence est de déterminer où se trouve l'utilisateur dans ce processus et de l'aider à progresser. Soyez flexible : si l'utilisateur veut simplement "y aller au feeling" sans lancer un tas d'évaluations formelles, vous pouvez le faire aussi.

## Communiquer avec l'utilisateur
Le créateur de compétences peut être utilisé par des personnes ayant des niveaux de familiarité très variables avec le jargon du code. Soyez attentif au contexte pour savoir comment formuler vos messages. Si vous avez un doute, expliquez brièvement les termes techniques (comme "JSON", "assertion", "benchmark").

---

## Étape 1 — Créer une compétence (Cerner l'intention)

**Cerner l'intention**
Commencez par comprendre l'intention de l'utilisateur. Posez des questions ciblées :
1. Que doit permettre de faire cette compétence ? (le résultat concret)
2. Quand doit-elle se déclencher ? (contextes, phrases)
3. Quel est le format de sortie attendu ?
4. Faut-il des cas de test ? Les compétences à sortie objective (code, data) en bénéficient. Celles à sortie subjective (style, art) non.

**Recherche et Interview**
Si besoin, utilisez des MCP ou des recherches en ligne pour trouver des informations utiles. Venez préparé pour réduire la charge sur l'utilisateur.

---

## Étape 2 — Rédiger le SKILL.md

### Le système de divulgation progressive
Une compétence bien conçue respecte cette structure :
```
nom-de-la-competence/
├── SKILL.md (obligatoire)
│   ├── En-tête YAML (name, description)
│   └── Instructions en Markdown (idéalement < 500 lignes)
└── Ressources associées (optionnelles)
    ├── scripts/     - Code exécutable
    ├── references/  - Documents chargés en contexte à la demande
```

### La Description (Le levier le plus important)
Le champ `description` dans l'en-tête YAML est le mécanisme **principal** qui détermine si l'agent va consulter la compétence. Elle doit être un peu "insistante".
- ❌ Faible : *"Permet de construire un tableau de bord."*
- ✅ Bon : *"Permet de construire rapidement un tableau de bord. À utiliser systématiquement dès que l'utilisateur mentionne un tableau de bord, des métriques internes, ou souhaite afficher des données, même s'il ne demande pas de 'dashboard'."*

### Style et patterns d'écriture (Méthode POSER)
- Préférer l'impératif ("Rédige...", "Vérifie...").
- Expliquer le POURQUOI plutôt que d'empiler des "TOUJOURS/JAMAIS" en majuscules.
- Définir un format de sortie strict si nécessaire.
- Donner des exemples (pattern Entrée/Sortie).
- Garder le principe de "non-surprise" (sécurité).

Utilisez la méthode POSER pour relire votre brouillon : **P**ersona, **O**bjectif, **S**ituation, **E**xclusions, **R**éférences.

---

## Étape 3 — Exécuter et évaluer les cas de test

Après avoir rédigé le brouillon, imaginez 2-3 prompts de test réalistes. Ne rédigez pas d'assertions pour le moment, juste les prompts. Enregistrez-les dans `evals/evals.json`. Exemple de bon cas de test : *"Mon manager vient de m'envoyer ce fichier xlsx (Q4_ventes_final_v2.xlsx) et veut que j'ajoute une colonne pour la marge en %."*

Cette section est une séquence continue — ne vous arrêtez pas en cours de route. N'utilisez AUCUNE compétence de test externe (comme `/skill-test`).

Placez les résultats dans `<nom-competence>-workspace/`. Organisez par itération (`iteration-1/`, etc.) et par test (`eval-0/`, etc.).

### 1: Lancer tous les tests (avec compétence ET baseline) dans le même tour
Pour chaque cas de test, lancez DEUX sous-agents (subagents) en parallèle : un avec la compétence, un sans. (Si vous êtes sur Claude.ai sans sous-agents, lisez la section correspondante plus bas).
- **Avec compétence** : `Save outputs to: <workspace>/iteration-<N>/eval-<ID>/with_skill/outputs/`
- **Baseline (sans/ancienne compétence)** : `Save to: without_skill/outputs/` ou `old_skill/outputs/`.

Rédigez un `eval_metadata.json` descriptif pour chaque cas de test.

### 2: Pendant que les tests tournent, rédiger les assertions
Rédigez des assertions quantitatives pour chaque cas de test et expliquez-les à l'utilisateur. Mettez à jour `eval_metadata.json` et `evals/evals.json`. 

### 3: Capturer les données de timing
Dès qu'un sous-agent termine, enregistrez ses données de temps et de tokens dans `timing.json`.

### 4: Noter, agréger et lancer le Viewer
1. **Noter** : Lancez un sous-agent "grader" (ou notez vous-même) pour évaluer chaque assertion. Enregistrez dans `grading.json`.
2. **Agréger** : Lancez `python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>`
3. **Analyse** : Regardez les résultats agrégés pour identifier des tendances.
4. **Lancer le Viewer** :
   ```bash
   nohup python <createur-de-competences-path>/eval-viewer/generate_review.py \
     <workspace>/iteration-N \
     --skill-name "my-skill" \
     --benchmark <workspace>/iteration-N/benchmark.json \
     > /dev/null 2>&1 &
   VIEWER_PID=$!
   ```
   (Pour des environnements sans écran/Cowork, utilisez `--static <output_path>` pour générer un fichier HTML autonome).
5. Demandez à l'utilisateur d'examiner les résultats (onglet Outputs et Benchmark) et de laisser des commentaires.

### 5: Lire les retours
Lisez `feedback.json` généré par l'utilisateur. Tuez le serveur viewer (`kill $VIEWER_PID`).

---

## Étape 4 — Améliorer la compétence (Itérer)

1. **Généraliser** : Cherchez la cause profonde des erreurs plutôt que de mettre des rustines "SURTOUT NE JAMAIS".
2. **Garder le prompt maigre** : Supprimez ce qui ne sert à rien.
3. **Expliquer le pourquoi** : Les LLM modernes comprennent mieux si on leur explique le contexte.
4. **Chercher le travail répété** : Si tous les tests génèrent le même script Python, packagez ce script dans `scripts/` de la compétence !

Une fois améliorée :
- Appliquez les changements au SKILL.md.
- Relancez tous les cas de test dans `iteration-<N+1>/`.
- Relancez le viewer avec `--previous-workspace`.
- Recommencez jusqu'à ce que l'utilisateur soit satisfait.

---

## Optimisation de la Description (Optionnel)

Après avoir terminé la compétence, proposez d'optimiser la description pour le triggering.
1. Générez 20 requêtes d'évaluation (JSON avec `query` et `should_trigger` : 10 vrais et 10 faux). Les faux positifs doivent être subtils.
2. Examinez cet ensemble avec l'utilisateur via le template HTML `assets/eval_review.html`.
3. Lancez la boucle d'optimisation en arrière-plan :
   ```bash
   python -m scripts.run_loop \
     --eval-set <path-to-trigger-eval.json> \
     --skill-path <path-to-skill> \
     --model <model-id> \
     --max-iterations 5 \
     --verbose
   ```
4. Appliquez la `best_description` résultante au SKILL.md.

---

## Packaging

Si vous avez accès à l'outil `present_files` ou un terminal, packagez la compétence :
```bash
python -m scripts.package_skill <path/to/skill-folder>
```
Indiquez à l'utilisateur où se trouve le fichier `.skill` pour qu'il l'installe.

---

## Spécificités selon les environnements

**Claude.ai (Sans sous-agents ni terminal complet)** :
- **Tests** : Vous devez accomplir les tâches de test vous-même de façon séquentielle. Ignorez les tests de baseline.
- **Revue** : Affichez les résultats directement dans le chat. Demandez des retours en direct ("Qu'en penses-tu ?").
- **Optimisation de la description** : Ignorez cette étape.
- **Mise à jour d'une compétence existante** : Copiez la compétence dans `/tmp/` avant de l'éditer, car les chemins d'installation sont souvent en lecture seule.

**Cowork / Antigravity (Avec sous-agents mais sans écran web direct)** :
- Vous avez des sous-agents, donc toute la logique d'exécution parallèle fonctionne.
- Utilisez `--static <output_path>` avec `generate_review.py` pour générer un fichier HTML autonome, et donnez le lien à l'utilisateur. Le bouton "Submit All Reviews" téléchargera un `feedback.json`.
- Mettez toujours "Créer les JSON d'eval et lancer `generate_review.py`" dans votre liste de tâches pour ne pas oublier l'intervention humaine !

---

## Fichiers de référence fournis

Le dossier `createur-de-competences/` inclut plusieurs scripts et guides :
- `agents/grader.md`, `agents/comparator.md`, `agents/analyzer.md` — Comment évaluer, comparer et analyser les résultats.
- `references/schemas.md` — Les structures JSON requises pour les évaluations.

**Rappel de la boucle principale :**
1. Comprendre l'intention.
2. Rédiger le brouillon du SKILL.md.
3. Lancer les agents sur les tests de validation.
4. Évaluer avec l'utilisateur via `generate_review.py`.
5. Répéter jusqu'à succès, puis packager.
