---
name: createur-de-competences
description: Compétence à consulter systématiquement dès qu'il s'agit de concevoir, rédiger, corriger ou améliorer une compétence (skill) pour Claude, Antigravity ou autre — que la demande soit "crée une compétence pour...", "transforme ce workflow en skill", "améliore cette compétence", "vérifie le format de ce SKILL.md", ou même une simple envie d'automatiser une tâche récurrente qui pourrait devenir une compétence réutilisable. Utilise-la aussi pour optimiser le déclenchement (triggering) d'une compétence existante ou pour l'évaluer avant de la livrer. À utiliser même si l'utilisateur ne prononce pas explicitement le mot "compétence" ou "skill".
---

# Créateur de compétences

Cette compétence guide la conception de nouvelles compétences (skills) pour Claude, ou l'amélioration de compétences existantes, en français, dans le respect du format et des bonnes pratiques attendues.

Une compétence bien conçue doit être : **claire** (Claude comprend immédiatement quoi faire), **cohérente** (elle ne se contredit pas, elle reste centrée sur un seul objectif) et **directement utilisable** (aucune étape manquante, aucun format ambigu).

**SKILL.md est un standard ouvert et portable** : plusieurs agents (Claude, mais aussi par exemple Google Antigravity/Gemini) lisent ce même format — un dossier contenant un `SKILL.md` avec en-tête YAML `name`/`description`, plus des ressources optionnelles. Les principes de cette compétence s'appliquent donc largement d'un agent à l'autre. Seuls les **emplacements de stockage** changent selon l'agent : chez Claude, les compétences vivent typiquement sous `/mnt/skills/public` (compétences intégrées), `/mnt/skills/user` (compétences personnelles installées) ou `/mnt/skills/examples`, alors que d'autres agents utilisent leurs propres chemins (ex. `.agents/skills/` pour un espace de travail, ou un dossier de config global). Si tu écris une compétence destinée à un autre agent que Claude, garde le format SKILL.md identique mais adapte le chemin d'installation en conséquence.

---

## Vue d'ensemble du processus

1. **Cerner l'intention** — comprendre précisément ce que la compétence doit permettre de faire.
2. **Interroger et rechercher** — poser les questions nécessaires avant d'écrire quoi que ce soit.
3. **Rédiger le SKILL.md** — en respectant l'anatomie et le format attendus.
4. **Tester** — imaginer 2-3 cas d'usage réalistes et vérifier que la compétence fonctionne.
5. **Itérer** — améliorer sur la base des retours, sans jamais complexifier inutilement.

Il n'est pas nécessaire de suivre ces étapes de façon rigide et séquentielle : si l'utilisateur a déjà un brouillon, on peut sauter directement à l'étape de test/amélioration. Si l'utilisateur veut simplement "y aller au feeling" sans process formel, c'est possible aussi.

---

## Étape 1 — Cerner l'intention

**Une compétence doit exceller dans un domaine précis.** Plutôt que de viser une compétence "couteau suisse" qui fait un peu de tout, mieux vaut créer plusieurs compétences distinctes, chacune ciblée sur une tâche bien identifiée. Si en cernant l'intention tu te rends compte que la demande couvre en réalité 2-3 besoins assez différents, propose à l'utilisateur de les scinder en compétences séparées plutôt que d'en faire une seule trop diffuse.

Avant d'écrire, il faut pouvoir répondre à ces questions (si la conversation contient déjà les réponses — par exemple l'utilisateur dit "transforme ce que je viens de faire en compétence" — les extraire directement du fil de discussion plutôt que de redemander) :

1. **Que doit permettre de faire cette compétence ?** (le résultat concret attendu)
2. **Quand doit-elle se déclencher ?** (quelles phrases, quels contextes utilisateur)
3. **Quel est le format de sortie attendu ?** (document, code, tableau, réponse structurée…)
4. **Faut-il des cas de test ?** Les compétences à sortie objectivement vérifiable (transformation de fichiers, génération de code, étapes de workflow fixes) en bénéficient. Les compétences à sortie subjective (style d'écriture, créativité) en ont rarement besoin.

Si des informations manquent, poser des questions ciblées sur les cas limites, les formats d'entrée/sortie, les exemples concrets et les critères de réussite — plutôt que de deviner.

---

## Étape 2 — Anatomie d'une compétence

```
nom-de-la-competence/
├── SKILL.md (obligatoire)
│   ├── En-tête YAML (name, description — obligatoires)
│   └── Instructions en Markdown
└── Ressources associées (optionnelles)
    ├── scripts/     - Code exécutable pour les tâches déterministes/répétitives
    ├── references/  - Documents chargés en contexte à la demande
    └── assets/      - Fichiers utilisés dans le résultat final (modèles, icônes, polices)
```

### Le système de divulgation progressive

Une compétence se charge en trois niveaux :

1. **Métadonnées** (`name` + `description`) — toujours en contexte, ~100 mots. C'est le SEUL élément que Claude ou Antigravity voit en permanence pour décider s'il doit consulter la compétence.
2. **Corps du SKILL.md** — chargé en contexte uniquement quand la compétence se déclenche (idéalement < 500 lignes).
3. **Ressources associées** — chargées à la demande, sans limite de taille ; les scripts peuvent s'exécuter sans être chargés en contexte.

**Bonnes pratiques associées :**
- Garder le SKILL.md sous les 500 lignes ; si on approche de cette limite, ajouter un niveau de hiérarchie supplémentaire (fichiers de référence) avec des indications claires sur quand les consulter.
- Toujours référencer clairement les fichiers annexes depuis le SKILL.md, avec le contexte de quand les lire.
- Pour les fichiers de référence volumineux (>300 lignes), inclure une table des matières.

**Organisation par domaine** : si une compétence couvre plusieurs variantes (frameworks, formats…), organiser par sous-fichier :
```
deploiement-cloud/
├── SKILL.md (workflow + logique de sélection)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```
Claude ou Antigravity ne lit alors que le fichier de référence pertinent pour le cas en cours.

### Les scripts comme des "boîtes noires"

Si la compétence embarque des scripts dans `scripts/`, indique explicitement dans le SKILL.md de les **exécuter directement** (éventuellement avec `--help` pour en découvrir les options) plutôt que de lire tout le code source avant de s'en servir. Cela évite de gaspiller du contexte et garde l'agent concentré sur la tâche plutôt que sur la compréhension de l'implémentation.

### Arbres de décision pour les compétences complexes

Dès qu'une compétence peut s'appliquer à plusieurs situations différentes (plusieurs formats de sortie possibles, plusieurs approches selon le contexte), ajoute une section qui aide explicitement à choisir la bonne branche à suivre. Par exemple :

```markdown
## Quelle approche utiliser ?
- Si l'utilisateur fournit un fichier .csv → suis la section "Import CSV"
- Si l'utilisateur fournit un fichier .xlsx → suis la section "Import Excel"
- Si aucun fichier n'est fourni → demande le format avant de continuer
```
Cela évite que l'agent choisisse une branche au hasard ou mélange plusieurs approches incompatibles.

---

## Étape 3 — Rédiger le SKILL.md

### Le champ `description` : le levier le plus important

C'est le mécanisme **principal** qui détermine si Claude ou Antigravity va consulter la compétence. Toutes les informations sur "quand l'utiliser" doivent se trouver ici — pas dans le corps du document.

Claude ou Antigravity a naturellement tendance à **sous-déclencher** les compétences (ne pas les consulter alors qu'elles seraient utiles). Pour compenser, la description doit être un peu "insistante" :

- ❌ Faible : *"Permet de construire un tableau de bord pour visualiser des données internes."*
- ✅ Bon : *"Permet de construire rapidement un tableau de bord pour visualiser des données internes. À utiliser systématiquement dès que l'utilisateur mentionne un tableau de bord, une visualisation de données, des métriques internes, ou souhaite afficher un type quelconque de données d'entreprise, même s'il ne demande pas explicitement un 'dashboard'."*

La description doit contenir :
- **Ce que fait la compétence** (l'action concrète)
- **Quand la déclencher** (contextes, formulations typiques, même indirectes)

**Rédige la description à la troisième personne** ("Génère...", "Aide à...", "Revoit...") plutôt qu'à la deuxième personne ("Je t'aide à..."). C'est une convention partagée par les principales implémentations du standard SKILL.md (Claude, mais aussi Google Antigravity) : la description est lue par l'agent lui-même pour décider s'il doit consulter la compétence, pas par l'utilisateur — elle doit donc se lire comme une fiche technique objective plutôt que comme une adresse directe.

### Le corps du document

- **name** : identifiant de la compétence (court, en minuscules, tirets)
- **description** : voir ci-dessus
- **compatibility** *(optionnel, rarement nécessaire)* : outils ou dépendances requis
- **le reste** : les instructions elles-mêmes

---

## Étape 4 — Style et patterns d'écriture

### Préférer l'impératif
Les instructions doivent être formulées à l'impératif : "Rédige...", "Vérifie...", "Structure la réponse ainsi...".

### Expliquer le POURQUOI plutôt que d'empiler des "TOUJOURS/JAMAIS" en majuscules
Les modèles actuels ont une bonne théorie de l'esprit : s'ils comprennent *pourquoi* une règle existe, ils l'appliquent mieux et savent l'adapter aux cas non prévus. Une compétence truffée de TOUJOURS / JAMAIS en capitales est un signal d'alerte — c'est souvent le signe qu'on a réagi à un cas précis au lieu de généraliser le principe sous-jacent.

### Définir un format de sortie
```markdown
## Structure du rapport
Utilise TOUJOURS ce gabarit exact :
# [Titre]
## Résumé exécutif
## Constats clés
## Recommandations
```

### Donner des exemples (pattern Entrée/Sortie)
```markdown
## Format des messages de commit
**Exemple 1 :**
Entrée : Ajout de l'authentification utilisateur avec des tokens JWT
Sortie : feat(auth): implémentation de l'authentification par JWT
```
3 à 5 exemples concrets (bons ET mauvais, sur le modèle de la méthode POSER — section Références) permettent d'aligner très efficacement le style et le format attendus.

### Rester général, pas seulement adapté à un cas précis
Écrire un premier brouillon, puis le relire à froid pour vérifier qu'il fonctionnerait sur des dizaines de variantes du même besoin, pas uniquement sur l'exemple qui a motivé sa création.

### Principe de "non-surprise" (sécurité)
Une compétence ne doit jamais faire quelque chose que son intitulé et sa description ne laisseraient pas prévoir. Ne jamais concevoir de compétence facilitant un accès non autorisé, l'exfiltration de données, du contenu malveillant, ou tout autre usage trompeur — même si un jeu de rôle explicite ("joue le rôle de...") reste parfaitement acceptable.

---

## Étape 5 — Cas de test

Après le brouillon, imaginer 2-3 prompts réalistes — le genre de phrase qu'un vrai utilisateur taperait, avec du contexte concret (noms de fichiers, chiffres, situation). Les proposer à l'utilisateur avant de les exécuter : *"Voici quelques cas de test que j'aimerais essayer, ça te convient ou tu veux en ajouter ?"*

**Mauvais cas de test** (trop abstraits) : "Formate ces données", "Extrais le texte du PDF"
**Bon cas de test** (concret, avec contexte) : "Mon manager vient de m'envoyer ce fichier xlsx (dans mes téléchargements, ça s'appelle un truc comme 'Q4_ventes_final_FINAL_v2.xlsx') et il veut que j'ajoute une colonne pour la marge en %. Le chiffre d'affaires est en colonne C et les coûts en colonne D je crois"

Exécuter ensuite la compétence sur ces cas, et présenter le résultat à l'utilisateur pour retour — sans supposer que c'est parfait du premier coup.

---

## Étape 6 — Itérer

1. Appliquer les améliorations demandées.
2. Rejouer les cas de test.
3. Chercher les motifs répétés : si plusieurs cas de test amènent Claude à réinventer le même script ou la même méthode, c'est le signal qu'il faut packager ce script une bonne fois dans `scripts/` plutôt que de le laisser réécrire à chaque fois.
4. Garder le prompt "maigre" : supprimer ce qui ne sert à rien. Si une partie de la compétence pousse Claude à perdre du temps sur des étapes improductives, la couper et observer le résultat.
5. Généraliser plutôt que rustiner : face à un problème récurrent, mieux vaut changer d'angle ou de métaphore que d'empiler des contraintes de plus en plus rigides.

Continuer jusqu'à ce que l'utilisateur soit satisfait, que les retours soient tous positifs, ou qu'il n'y ait plus de progrès significatif.

---

## Gabarit vierge à copier pour démarrer

```markdown
---
name: nom-de-la-competence
description: [Ce que fait la compétence] + [Quand la déclencher, de façon insistante et avec des reformulations variées]
---

# [Titre de la compétence]

[Une phrase expliquant l'objectif general et pourquoi cette compétence existe.]

## [Section 1 : ex. Processus / Étapes]
...

## [Section 2 : ex. Format de sortie attendu]
...

## [Section 3 : ex. Exemples (bons et mauvais)]
...

## [Section 4 : ex. Ce qu'il faut éviter, avec l'alternative]
...
```

---

## Rappel express (méthode POSER appliquée à la compétence elle-même)

Quand tu rédiges une compétence, tu peux te servir de la méthode POSER comme grille de relecture finale :
- **P**ersona : le corps du SKILL.md donne-t-il assez de cadrage sur le rôle/niveau d'exigence attendu ?
- **O**bjectif : le but de la compétence est-il énoncé clairement dès le début ?
- **S**ituation : les contraintes réelles (longueur, public, format de sortie) sont-elles précisées ?
- **E**xclusions : les pièges à éviter sont-ils listés, chacun avec son alternative positive ?
- **R**éférences : y a-t-il 3 à 5 exemples concrets (bons/mauvais) pour ancrer le style ?

Si l'une de ces cases est vide, c'est probablement là qu'il faut compléter la compétence avant de la livrer.
