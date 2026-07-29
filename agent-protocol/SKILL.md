---
name: agent-protocol
description: Protocole d'orchestration POSER v4 pour piloter, du cadrage à la livraison, la création de tout projet web/logiciel — SaaS, dashboard, landing page, CV/portfolio, site vitrine, storefront, automatisation, pipeline de données, agent IA/MCP, jeu navigateur — dans Claude Code ou Antigravity. Pipeline en 6 jalons (Cadrage → Plan → Architecture → Design → Construction → Tests/Livraison), architecture Directive/Orchestration/Exécution, routeur de skills par type de projet. Dès qu'un écran/UI est concerné, le Jalon Design pose d'abord une question de confirmation. Claude Design (handoff + arrêt de session) reste la voie par défaut, repli sur les skills internes si l'utilisateur confirme ne pas pouvoir l'utiliser. Utiliser dès qu'on demande de construire, concevoir, coder ou livrer une application, un site, un dashboard, un SaaS ou une automatisation — même sans mention de "protocole". Ne pas utiliser pour de simples questions de code sans livrable complet.
---

# AGENT-PROTOCOL — Protocole POSER v4

> **But** : livrer un projet fiable (site, SaaS, dashboard, landing, automatisation, pipeline, agent IA...) en minimisant les appels, le contexte chargé et les modifications inutiles.
> Cette compétence est le **chef d'orchestre unique** : elle indique QUAND lire quoi, QUELLES compétences/modules mobiliser à chaque phase, et COMMENT ne jamais relire deux fois la même chose.
> **Règle d'adaptation** : le dépôt du projet est la source de vérité. Les skills externes (globaux) ne sont utilisés qu'après une découverte courte et ciblée. Ne jamais inventer un outil, une commande ou une intégration.
> **Fichiers de référence** (à charger uniquement quand le jalon concerné les requiert) : `references/design-modules.md` (Jalon D), `references/audit-securite.md` (Jalon F), `references/exemple-facturation.md` (illustration).

---

## 0. Modèle Mental — Pourquoi 3 couches

Les LLMs sont probabilistes ; la logique métier récurrente exige, elle, de la cohérence déterministe. 90% de précision par étape probabiliste = 59% de réussite cumulée sur 5 étapes. **On pousse donc la complexité répétable dans du code déterministe**, et l'agent se concentre uniquement sur la décision.

| Couche | Rôle | Où |
|---|---|---|
| **Directive** (quoi faire) | SOP en langage naturel : objectif, entrées, outils/scripts, sorties, cas limites | `directives/*.md` |
| **Orchestration** (décider) | **C'est vous.** Lire la directive, appeler le bon outil/script dans le bon ordre, gérer les erreurs, demander des clarifications, mettre à jour la directive avec les apprentissages | — |
| **Exécution** (faire) | Scripts déterministes, testables, rapides, bien commentés | `execution/*.py` |

Cette séparation s'applique **chaque fois qu'une sous-tâche est répétable et déterministe** (scraping, appel API, export, transformation de données, batch, intégration Sheets/Slides). Pour du code applicatif one-shot (UI, logique métier propre au produit), on code directement dans le projet — pas besoin de fiche `directives/` séparée, seul le pipeline à jalons (section 6) s'applique.

### Contrat opérationnel (à respecter à CHAQUE tâche)
1. **Lire avant d'écrire** : `README*`, config projet, instructions locales (`AGENTS.md`, `CLAUDE.md`), état Git (`git status`, `git log --oneline -5`). Pas de lecture récursive intégrale du dépôt.
2. **Vérifier `execution/` avant d'écrire un script.** Ne créer un nouveau script que si aucun n'existe déjà pour ce besoin.
3. **Découvrir les capacités une seule fois par session.** Lire les `SKILL.md` pertinents (nom, description, prérequis, outils, limites) — pas le code source complet sauf blocage.
4. **Sélectionner peu d'outils** : 1–3 skills complémentaires par étape, en priorisant l'existant.
5. **Travailler par jalons/lots.** Passer au jalon suivant seulement après le critère de sortie. Validation humaine uniquement pour décisions irréversibles, coûteuses ou ambiguës.
6. **Changements atomiques** : petits lots, formatage, tests ciblés, vérification. Pas de refactor hors périmètre.
7. **Jamais de secrets exposés** : ni valeurs `.env`, ni clés, ni identifiants à l'écran ou dans un fichier commité. Utiliser `.env.example`.
8. **Rendre compte brièvement** : faits, fichiers modifiés, validations exécutées, risques — pas de journal exhaustif.
9. **Une seule source de vérité** : décisions validées → `docs/decisions.md`. Le lire plutôt que redemander le contexte.
10. **Auto-correction quand ça casse** : lire l'erreur/trace → corriger le script → retester (sauf tokens/crédits payants : vérifier avec l'utilisateur d'abord) → **mettre à jour la directive** correspondante avec la contrainte apprise (limite API, timing, edge case).
11. **Skill/directive manquante** : le signaler à l'utilisateur au lieu d'improviser silencieusement.
12. **Ne jamais créer/écraser une directive** sans demander, sauf instruction explicite — ce sont des documents vivants, à préserver et enrichir dans le temps.

### Budget de contexte
- Résumé opérationnel ≤ 250 mots pour démarrer.
- Chemins, extraits ciblés, résultats synthétiques > gros dumps.
- Documentation : squelette d'abord, puis remplir seulement les rubriques affectées.
- Incertitude bloquante → **≤ 3 questions regroupées**. Sinon, hypothèse réversible + avancer.
- **Pas de sur-planification** : profondeur du plan proportionnelle à la taille du projet.

---

## 1. Entrée Projet — Remplir ou Inférer avec Prudence

```yaml
projet:
  type: automation | saas | landing-page | dashboard | cv-portfolio | jeu-navigateur | design-to-code | fullstack | storefront | site-web | video-motion | agent-ia | data-pipeline | autre
  objectif: ""
  utilisateur_cible: ""
  resultat_mesurable: ""          # ex: "500ms de temps de chargement", "taux de conversion > 3%"
  contraintes:
    - budget/delai: ""
    - stack_hebergement_impose: ""
    - securite_confidentialite: ""
  sources_donnees_et_integrations: []
  definition_de_fini: []          # critères vérifiables qui signent la livraison
```
> Si absent : produire une **fiche d'hypothèses** (≤ 8 lignes) et ne demander que ce qui empêche de démarrer.

**Si l'utilisateur fournit un document existant** (esquisse, brief, compte-rendu, notes de réunion, ancien cahier des charges...) : le lire en premier et en extraire directement les champs ci-dessus, sans redemander ce qui y figure déjà. Ne poser de question que sur les champs réellement absents et bloquants. Si le document couvre déjà l'essentiel, sauter la reformulation manuelle et soumettre directement la fiche YAML complétée à validation avant d'entamer le Jalon A.

---

## 2. Structure de Fichiers Unifiée

```
/ (racine du projet)
├── AGENT-PROTOCOL.md / .claude/skills/agent-protocol/  ← cette compétence
├── AGENTS.md / CLAUDE.md   ← pointent vers cette compétence
├── .env                     ← secrets (jamais commité) · .env.example documenté
├── docs/
│   ├── brief.md             ← Jalon A
│   ├── plan.md              ← Jalon B
│   ├── architecture.md      ← Jalon C (si complexité le justifie)
│   ├── design-spec.md       ← Jalon D
│   ├── changelog.md         ← Jalon E (par lot, si écart avec le plan)
│   ├── decisions.md         ← source de vérité des choix figés
│   └── audit.md             ← Jalon F (rapport de livraison)
├── directives/               ← SOP Markdown pour sous-tâches déterministes récurrentes
│   └── <tache>.md
├── execution/                 ← scripts Python déterministes, testés, commentés
│   └── <script>.py
└── .tmp/                      ← intermédiaires jetables, jamais commités, toujours régénérés
```

**Livrables vs Intermédiaires** : un livrable est ce que l'utilisateur peut ouvrir/consulter (code applicatif du projet, Google Sheets/Slides, export). Un intermédiaire (dossier scrapé, cache, export temporaire) reste dans `.tmp/`.

---

## 3. Référentiel des Skills Disponibles par Famille

> Chemin type : `{{SKILLS_DIR}}/<nom-du-skill>/SKILL.md` — sur Antigravity : `~/.gemini/config/skills/` ; sur Claude Code : dossier `skills/` ou `.claude/skills/` du projet/utilisateur. Toujours vérifier le chemin réel de l'environnement en cours plutôt que le supposer. Ne jamais inventer un skill absent.

### 🧠 Stratégie & Workflow
| Skill | Usage |
|---|---|
| `brainstorming` | Exploration de besoins avant implémentation |
| `planification` | Plans d'implémentation multi-étapes avec TDD |
| `skill-creator` / `skill-repair` | Créer, améliorer, réparer des compétences |
| `accidental-data-loss-prevention` | Confirmation avant opération destructive |

### 🎨 Design & UI/UX
| Skill | Usage |
|---|---|
| **Claude Design** | Voie par défaut du Jalon D, confirmée par une question explicite à l'utilisateur — voir section 6, Jalon D |
| `stitch` | Repli légitime si l'utilisateur répond Non à la question de confirmation Claude Design |
| `ui-ux-pro-max` | Recommandations UX, patterns, palettes, typographies |
| `design` / `design-system` | Identité visuelle complète / tokens de design |
| `frontend-design` | Direction visuelle intentionnelle |
| `brand` / `brand-guidelines` | Identité de marque, messaging, charte |
| `canvas-design` / `banner-design` | Visuels statiques, bannières réseaux sociaux |
| `theme-factory` / `ui-styling` | Thème rapide cohérent / composants shadcn+Tailwind |
| `algorithmic-art` | Art génératif p5.js |
| Modules internes | `landing-cinematique`, `cv-cinematique`, `saas-designer` — voir `references/design-modules.md` |

### 💻 Développement Web & Frontend
| Skill | Usage |
|---|---|
| `modern-web-guidance` | Bonnes pratiques HTML/CSS/JS/APIs |
| `web-artifacts-builder` | Artefacts React complexes (shadcn/ui, routing, state) |
| `chrome-extensions` | Extensions Chrome Manifest V3 |
| `mcp-builder` | Création de serveurs MCP |
| `claude-api` | Intégration API Anthropic (streaming, tools, agents) |
| `google-antigravity-sdk` | Agents multi-agents SDK Antigravity |

### 🧪 Tests & Débogage
| Skill | Usage |
|---|---|
| `webapp-testing` | Tests fonctionnels Playwright |
| `a11y-debugging` | Audit accessibilité (ARIA, contraste, clavier) |
| `debug-optimize-lcp` | Core Web Vitals (LCP/CLS/INP) |
| `memory-leak-debugging` | Fuites mémoire JS/Node |
| `chrome-devtools` / `troubleshooting` | Débogage navigateur via DevTools MCP |
| Module interne | `audit-securite-vibe-code` — voir `references/audit-securite.md` |

### 📄 Documents & Data
| Skill | Usage |
|---|---|
| `doc-coauthoring`, `docx`, `pdf`, `pptx`, `xlsx`, `slides`, `internal-comms` | Documents, présentations, tableurs |
| `building-data-apps`, `bigquery`, `data-autocleaning`, `gcp-data-pipelines`, `dbt-bigquery`, `firestore-data`, `ml-best-practices`, `managing-python-dependencies` | Dashboards data, pipelines, ML, dépendances Python |
| `remotion-best-practices`, `slack-gif-creator` | Vidéo/motion, GIFs |
| Bases de données : `alloydb-*`, `cloud-sql-*`, `spanner-data` | Selon moteur choisi |

---

## 4. Découverte Ciblée des Skills (une fois par session)

1. Lire `README*`, `AGENTS.md`, `CLAUDE.md`, `git log --oneline -5`.
2. Rechercher par intention : `brainstorm`, `planning`, `architecture`, `ui`, `frontend`, `design`, `database`, `auth`, `testing`, `e2e`, `deploy`, `security`, `browser`, `automation`, `mcp`.
3. Pour chaque candidat : lire nom, description, prérequis, outils exposés, limites — pas le code source complet.
4. Choisir les capacités qui apportent une valeur nette ; justifier en une ligne.

**Registre de session** (ne pas répéter si inchangé) :
```md
## Capacités retenues
| Jalon | Skill/Module | Usage précis | Pourquoi |
|-------|-------|-------------|---------|
| cadrage | brainstorming | exploration du besoin | requis avant implémentation |
| design | Claude Design / saas-designer | prototypage ou skill interne | selon dispo |
| construction | … | … | … |
| validation | … | … | … |
```

**Interdits** : installer un plugin/dépendance, appeler un service payant, accéder à une intégration externe, lancer un déploiement — sans consentement explicite. Skill absent → poursuivre avec les outils standards et le signaler.

---

## 5. Le Router de Projet

| Type de projet | Priorité | Jalon A-B | Jalon D (Design) | Jalon E (Dev) | Jalon F (Tests) | Complexité |
|---|---|---|---|---|---|---|
| **Automatisation** | fiabilité, idempotence | `brainstorming` `planification` | _(aucun)_ | couche `execution/` + `accidental-data-loss-prevention` | tests manuels + retry | Faible |
| **SaaS** | domaine, auth, données | `brainstorming` `planification` `ui-ux-pro-max` | Claude Design + `saas-designer` | `modern-web-guidance` `web-artifacts-builder` `claude-api` | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` audit sécurité | Élevée |
| **Landing page** | conversion, design, vitesse | `brainstorming` `ui-ux-pro-max` | Claude Design + `landing-cinematique` | `modern-web-guidance` | `a11y-debugging` `debug-optimize-lcp` | Très faible |
| **CV / Portfolio** | image personnelle, impact | `brainstorming` | Claude Design + `cv-cinematique` | `modern-web-guidance` | `a11y-debugging` | Très faible |
| **Dashboard / Data** | justesse et lecture des données | `brainstorming` `planification` | Claude Design + `saas-designer` `design-system` | `building-data-apps` `modern-web-guidance` | `webapp-testing` `debug-optimize-lcp` | Moyenne |
| **Jeu navigateur** | boucle jouable, réactivité | `brainstorming` `planification` | `frontend-design` `algorithmic-art` | `modern-web-guidance` `web-artifacts-builder` | `webapp-testing` `chrome-devtools` | Moyenne |
| **Design → Code** | fidélité, responsive, a11y | `brainstorming` `ui-ux-pro-max` | Claude Design + `frontend-design` `design-system` | `modern-web-guidance` `web-artifacts-builder` | `a11y-debugging` `debug-optimize-lcp` | Faible-moyenne |
| **Fullstack** | domaine, auth, données, E2E | `brainstorming` `planification` `ui-ux-pro-max` | Claude Design + `saas-designer` `frontend-design` | `modern-web-guidance` `web-artifacts-builder` `claude-api` `execution/` | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` audit sécurité | Élevée |
| **Storefront** | parcours d'achat sûr | `brainstorming` `planification` `ui-ux-pro-max` | Claude Design + `design-system` `frontend-design` | `modern-web-guidance` `web-artifacts-builder` | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` | Moyenne-élevée |
| **Site web (vitrine)** | design, SEO, vitesse | `brainstorming` `ui-ux-pro-max` | Claude Design + `frontend-design` `brand` | `modern-web-guidance` | `a11y-debugging` `debug-optimize-lcp` | Faible-moyenne |
| **Vidéo / Motion** | fluidité, rendu | `brainstorming` | `design-system` `canvas-design` | `remotion-best-practices` | validation manuelle | Faible |
| **Agent IA / MCP** | fiabilité, sécurité | `brainstorming` `planification` | _(aucun)_ | `claude-api` `mcp-builder` `google-antigravity-sdk` `execution/` | `webapp-testing` audit sécurité | Élevée |
| **Data Pipeline** | correctness, idempotence | `brainstorming` `planification` | _(aucun)_ | `gcp-data-pipelines` `execution/` `bigquery` | `gcp-pipeline-orchestration` | Élevée |

> Colonne "Jalon D" = intrants du fichier de handoff Claude Design (voie par défaut) **ou** skills exécutés directement si l'utilisateur répond Non à la question de confirmation (voir Jalon D, section 6). Dès qu'un type de projet comporte des écrans/UI (SaaS, Landing, CV, Dashboard, Design→Code, Fullstack, Storefront, Site web), la question de confirmation Claude Design est **toujours posée** avant de choisir la voie. Les types marqués `(aucun)` ou sans écran (Automatisation pure, Agent IA/MCP backend, Data Pipeline) n'ont pas de Jalon D à proprement parler.

---

## 6. Pipeline à Jalons (A → F)

### Jalon A — Cadrage, Brainstorming & Brief
**But** : transformer la demande en MVP testable, sans construire. **Skills** : `brainstorming` · `ui-ux-pro-max` (si UI) · `planification` (pré-cadrage)
```
[PERSONA] Consultant produit senior, créatif et pragmatique.
[OBJECTIF] Clarifier {{DESCRIPTION_IDEE}}. Produire un brief exploitable.
[SITUATION] Type : {{TYPE_PROJET}} | Cible : {{PUBLIC_CIBLE}} | Contraintes : {{CONTRAINTES}}
[SKILLS] 1. brainstorming → exploration (pas de code) 2. ui-ux-pro-max → 2-3 directions visuelles si UI
[EXCLUSIONS] Pas de code ni de choix de stack. Ne pas inventer de contrainte non donnée.
[ITÉRATION] ≤ 3 questions regroupées avant le brief final.
```
**`docs/brief.md`** : Problème/cible/promesse · MVP · Parcours principal · Critères d'acceptation vérifiables · Hypothèses/risques · Hors périmètre · Décisions à valider.
**Sortie** : parcours principal décrit sans ambiguïté sur les critères d'acceptation.

### Jalon B — Plan d'Exécution
**But** : décomposer en lots ordonnés, sans code. **Skills** : `planification` · `doc-coauthoring` · `slides` (si présentation)
```
[PERSONA] Chef de projet technique, livraisons itératives.
[OBJECTIF] Depuis docs/brief.md, produire un plan en 3–7 lots démontrables/testables.
[SITUATION] Consulter docs/decisions.md si existant + Router (section 5) pour {{TYPE_PROJET}}.
[EXCLUSIONS] Pas de code, pas de granularité excessive, réutiliser la stack existante.
[ITÉRATION] Proposer le plan, valider avant construction.
```
**`docs/plan.md`** : Décisions verrouillées · Lot 1 (fondations) · Lot 2 (flux principal) · Lot 3 (qualité/livraison) — chaque lot : action · fichiers touchés · validation · skill mobilisé · Dépendances/risques/rollback.
**Sortie** : ordre, dépendances et scénario de validation de chaque lot sont clairs.

### Jalon C — Architecture Juste Suffisante
**But** : figer les choix structurants, seulement si la complexité le justifie. **Skills** : `doc-coauthoring` · `managing-python-dependencies` (back Python) · skill DB selon choix
> ⚡ Landing/site simple : 3 lignes dans le plan, pas de fichier séparé.
```
[PERSONA] Architecte logiciel senior, anti sur-ingénierie.
[OBJECTIF] ADR léger pour {{TYPE_PROJET}} : stack, flux, intégrations. Base : brief + plan.
[EXCLUSIONS] Pas de composant non justifié. Justifier chaque choix en une phrase. Jamais de microservices pour une landing page.
[ITÉRATION] Plusieurs stacks plausibles → tableau comparatif → attendre arbitrage.
```
**`docs/architecture.md`** : Contexte/contraintes · Vue d'ensemble · Composants/responsabilités · Modèle de données/flux · Contrats (routes/événements) · Auth/secrets · Fiabilité (erreurs, idempotence, limites, observabilité) · Perf/a11y · Déploiement/rollback · ADR.

Exigences par domaine : **Automatisation** → déclencheur, état, retries/backoff, idempotence, rate limits, logs, alertes, reprise (→ formaliser en `directives/` + `execution/`). **SaaS/Fullstack** → frontières client/API, rôles, multi-tenant si requis, migrations, validation serveur, quotas, audit. **Dashboard** → provenance, fraîcheur, granularité, filtres, agrégations, états vide/erreur, export. **Jeu** → boucle, états, contrôles, sauvegarde, perf mobile, écran de fin. **Storefront** → catalogue, panier, stocks, taxes/livraison, paiement via prestataire (**ne jamais implémenter le traitement de carte soi-même**), confirmation, conformité.
**Sortie** : chaque composant a une responsabilité, chaque donnée critique un propriétaire, chaque défaillance prévisible une réponse.

### Jalon D — Design & Expérience Utilisateur (Claude Design par défaut, avec repli confirmé)
**But** : concevoir avant d'implémenter, au niveau adapté au produit.

> **Voie par défaut : Claude Design.** Dès qu'un écran/UI est concerné, le Jalon D commence toujours par une **question de confirmation obligatoire** à l'utilisateur — jamais une hypothèse silencieuse. Le repli sur les skills internes (`stitch`, `ui-ux-pro-max`, `design-system`, `frontend-design`, modules `landing-cinematique`/`cv-cinematique`/`saas-designer`) n'est légitime **que si l'utilisateur confirme explicitement** ne pas pouvoir/vouloir passer par Claude Design maintenant — jamais une décision prise seul par l'agent.

**Procédure, dans cet ordre exact :**

0. **Poser la question de confirmation**, en un seul appel, avant toute autre action du jalon :
   > *"Peux-tu passer par Claude Design maintenant pour cette étape ? Réponds Oui si tu peux lui transmettre le fichier de handoff et me rapporter le résultat, ou Non si tu préfères que je fasse le design directement avec les skills internes disponibles ici."*

1. **Si OUI** : compiler `docs/handoff-claude-design.md` à partir de `docs/brief.md`, `docs/plan.md`, `docs/architecture.md` (si existant), design system existant (Mode A/B/C, cf. `saas-designer`), preset esthétique pertinent (`landing-cinematique` / `cv-cinematique` / `saas-designer`, cf. `references/design-modules.md`), captures d'inspiration fournies. Contient le prompt prêt à coller dans Claude Design (persona, objectif, contraintes, livrables attendus — gabarit ci-dessous). **S'ARRÊTER** immédiatement après : ne pas enchaîner sur le Jalon E, ne pas générer de code frontend tant que le retour n'est pas reçu. Demander explicitement à l'utilisateur de rapporter le résultat (export, capture, spec, tokens, lien). **Reprendre uniquement à réception** : consigner dans `docs/design-spec.md`, clore le Jalon D, démarrer le Jalon E.

2. **Si NON** : ne pas s'arrêter. Produire directement `docs/design-spec.md` dans la session, en mobilisant les skills/modules disponibles — `stitch` (maquettes), `ui-ux-pro-max` (patterns UX), `design-system` (tokens), `frontend-design` (direction visuelle), et le module `landing-cinematique` / `cv-cinematique` / `saas-designer` pertinent selon le type de projet (`references/design-modules.md`) — puis enchaîner directement sur le Jalon E sans validation externe supplémentaire.

**Gabarit du fichier `docs/handoff-claude-design.md`** (uniquement si réponse OUI) :
```
[PERSONA] Designer produit senior, esthétique moderne, cohérence design system.
[OBJECTIF] Direction visuelle pour {{TYPE_PROJET}} avant tout code frontend.
[INTRANTS] Design system existant : {{OUI/NON + détails}} · Preset retenu : {{landing-cinematique |
  cv-cinematique | saas-designer | aucun}} (cf. references/design-modules.md) · Captures d'inspiration :
  {{jointes/aucune}} · Contraintes : {{ex. accessibilité, responsive, charte de marque}}
[LIVRABLES ATTENDUS DE CLAUDE DESIGN] Prototype/maquettes des écrans listés dans docs/plan.md,
  palette+typo+espacements+radius, inventaire des composants, états (chargement/vide/erreur/mobile).
[EXCLUSIONS] Pas de template générique. Chaque choix intentionnel.
[ITÉRATION] Proposer 2 directions distinctes → l'utilisateur choisit avant maquettes définitives.
```

| Besoin | Skill/Module | Rôle |
|---|---|---|
| Design system existant | Analyse codebase (`saas-designer` §Mode A/B/C) | Intrant Claude Design **ou** base directe si réponse NON |
| Preset esthétique | `landing-cinematique` / `cv-cinematique` / `saas-designer` (`references/design-modules.md`) | Intrant Claude Design **ou** exécuté directement si réponse NON |
| Direction visuelle/contraintes de style | `ui-ux-pro-max`, `frontend-design`, `brand` | Intrant Claude Design **ou** exécuté directement si réponse NON |
| Maquettes d'écrans | `stitch` | Intrant Claude Design **ou** exécuté directement si réponse NON |
| Assets statiques isolés (hors prototypage d'écran) | `canvas-design` / `banner-design` | Complémentaire dans les deux cas |

**`docs/design-spec.md`** (rédigé au retour de Claude Design, ou directement si réponse NON) : Direction retenue (palette/typo/espacements/radius) · Lien/export du prototype (si Claude Design) · Inventaire écrans/composants · Parcours/microcopies · Responsive (breakpoints) · Accessibilité · États (chargement/vide/erreur/non-autorisé/mobile).
Critères spécifiques : **Landing** → proposition de valeur sans scroll, CTA primaire, preuve de confiance, perf. **Dashboard** → 1 question métier par graphique, choix justifié, légendes, filtres. **Storefront** → recherche/catégories, fiche produit, panier, checkout clair, signaux de confiance.
**Sortie** : `docs/design-spec.md` produit (par Claude Design ou en interne selon la réponse), interface et états critiques constructibles sans nouvelle décision de design majeure. **Le Jalon E ne démarre jamais sans cette sortie ni sans être passé par la question de confirmation.**

### Jalon E — Construction Incrémentale
**But** : coder, tester, livrer, en respectant strictement plan, architecture et **prototype Claude Design** validés.

| Besoin | Skill |
|---|---|
| Frontend moderne | `modern-web-guidance` |
| Composants React complexes | `web-artifacts-builder` |
| Intégration Claude/Gemini | `claude-api` |
| Agent IA multi-composants | `google-antigravity-sdk` |
| Serveur MCP custom | `mcp-builder` |
| Sous-tâche déterministe récurrente (scraping, export, batch, intégration Sheets/Slides) | couche `directives/` + `execution/` (section 0) |
| Scripts Python + dépendances | `managing-python-dependencies` |
| Dashboard data / Pipeline / BigQuery / DB | `building-data-apps` / `gcp-data-pipelines` / `bigquery` / skill DB dédié |
| Opération destructive | `accidental-data-loss-prevention` ← **OBLIGATOIRE** |

```
[PERSONA] Développeur senior full-stack, livraisons par petites itérations testables.
[OBJECTIF] Implémenter le lot {{NUMERO_LOT}} de docs/plan.md, selon architecture/design validés.
[SÉQUENCE PAR TÂCHE]
a) Relire le lot concerné + conventions du repo
b) Si sous-tâche déterministe récurrente → vérifier execution/ ; script existant ? le réutiliser ;
   sinon écrire le script + une directive courte dans directives/ (entrées/sorties/limites)
c) Écrire le test qui échoue (TDD)
d) Implémenter le chemin le plus court, interfaces simples
e) Formatage, lint, tests ciblés → corriger les erreurs introduites
f) Commit
g) docs/changelog.md uniquement si la réalité diffère de la décision planifiée
[EXCLUSIONS] Ne pas toucher aux fichiers hors périmètre du lot. Ne pas réécrire architecture/design déjà validés.
[AVANT ACTION DESTRUCTIVE] accidental-data-loss-prevention → résumé 5 lignes → feu vert explicite.
```
**Qualité non négociable (chaque lot)** : entrées validées côté serveur, messages d'erreur utiles non sensibles · états chargement/vide/erreur visibles · HTML sémantique, clavier, focus, contraste · mocks/fixtures étiquetés comme tels · aucun secret dans Git · aucun `TODO` bloquant déguisé en fini.
**Résumé de lot obligatoire (5 lignes)** : Réalisé · Comment tester · Ce qui reste · Risques · Décision attendue.

### Jalon F — Vérification, Audit & Livraison
**But** : valider la qualité, corriger, déployer. **Skills** : `webapp-testing` · `a11y-debugging` · `debug-optimize-lcp` · `memory-leak-debugging` · `chrome-devtools` · module `audit-securite-vibe-code` (`references/audit-securite.md`) si SaaS/Fullstack/Auth/DB
```
[SÉQUENCE]
a) Formatage/lint  b) Vérification types/build  c) Tests unitaires ciblés puis complets si coût raisonnable
d) Test du parcours principal (E2E ou manuel)  e) Audit rapide : responsive, a11y, erreurs réseau, env vars
f) Si SaaS/Fullstack/DB/Auth → module audit sécurité (references/audit-securite.md)
g) Revue du diff Git (fichiers accidentels, changements hors périmètre)
Pour une automatisation : essai contrôlé, prouver le résultat, tester au moins un échec/retry.
[AVANT DÉPLOIEMENT] Présenter build command · variables d'env requises · migrations · rollback. Attendre autorisation explicite.
```
**`docs/audit.md`** : Réalisé · Parcours vérifié · Fichiers/composants majeurs · Validations exécutées et résultat · Configuration requise (sans secrets) · Limites/risques restants · Prochaine action suggérée.

---

## 7. Module — Audit de Sécurité Vibe-Code

> Contenu complet : `references/audit-securite.md`. À invoquer au Jalon F pour tout projet SaaS/Fullstack/Automatisation manipulant secrets, DB ou auth. Résumé : lire toute la codebase, verdict individuel par item de checklist (✅/❌/⚠/⬚), format de conclusion imposé (sévérité, CWE, code vulnérable, correction, effort), rapport final avec posture globale et plan de remédiation priorisé.

## 8. Modules de Design Internes

> Contenu complet : `references/design-modules.md`. Trois modules de repli/intrant pour Claude Design : `landing-cinematique` (§8.1), `cv-cinematique` (§8.2), `saas-designer` (§8.3) — à consulter au Jalon D quand le projet correspond exactement à l'un de ces types ou que Claude Design est indisponible.

## 9. Annexe — Exemple Bout-en-Bout Multi-Agents

> Contenu complet : `references/exemple-facturation.md`. Illustre l'enchaînement Jalons A→F d'un SaaS de facturation avec deux environnements (Claude pour la planification, Antigravity/Gemini pour la construction visuelle).

---

## 10. Invocations Compactes (à coller dans une nouvelle session)

**A. Démarrer/reprendre** :
```
Suis la compétence agent-protocol strictement. Objectif : [OBJECTIF]. Type : [TYPE].
Lis README*, AGENTS.md, git log --oneline -5. Identifie skills/modules pertinents sans scan massif.
Affiche le registre de capacités retenues + résumé opérationnel ≤ 250 mots.
Exécute uniquement le Jalon [A/B/C/D/E/F]. Arrête-toi au critère de sortie, ≤ 3 questions si décision bloquante.
```
**A bis. Démarrer à partir d'un brief/esquisse existant** :
```
Suis agent-protocol. Voici mon document de cadrage existant : [FICHIER/ESQUISSE JOINT].
Lis-le en premier, remplis la fiche YAML (section 1) à partir de son contenu,
ne me pose de question que sur les champs manquants et bloquants pour démarrer.
Soumets-moi la fiche complétée pour validation, puis enchaîne directement sur le Jalon [A/B/...].
```
**B. MVP de bout en bout** :
```
Suis agent-protocol. Construis : [OBJECTIF] (type [TYPE], cible [CIBLE], contraintes [CONTRAINTES]).
Découvre une fois les skills/modules pertinents (section 3 et 8). Jalons A→F avec gates :
soumets brief+plan+architecture pour validation si décision irréversible ; sinon hypothèse réversible + avance.
Au Jalon D : pose d'abord la question de confirmation Claude Design. Si Oui : produis
docs/handoff-claude-design.md puis ARRÊTE-TOI — attends mon retour avant le Jalon E.
Si Non : fais le design directement avec les skills internes, sans t'arrêter. Lots testés un par un, rapport final.
Pas d'installation/appel payant/déploiement sans accord explicite.
```
**C. Fonctionnalité sur dépôt existant** :
```
Suis agent-protocol en mode changement ciblé. Fonctionnalité : [FEATURE].
Lis le strict nécessaire, détecte les skills une fois, mini-plan ≤ 7 étapes avec validations,
implémente en petits lots, rapport final avec limites.
```
**D. Corriger un bug** :
```
Suis agent-protocol en mode diagnostic frugal. Symptôme : [SYMPTÔME].
Reproduis, isole la cause avec le moins de fichiers/outils possible, corrige a minima,
ajoute un test anti-régression. Conclusion : cause racine · correction · validations · risque résiduel.
```
**E. Préparer le Jalon D landing/CV cinématographique** :
```
Suis agent-protocol, Jalon D. Le projet est de type landing-page/cv-portfolio.
Pose d'abord la question de confirmation Claude Design.
Si Oui : pose en un seul appel les 4 questions du module pertinent (references/design-modules.md
§8.1 landing ou §8.2 CV), compile docs/handoff-claude-design.md avec preset+architecture figée
comme intrants, puis ARRÊTE-TOI et attends le retour.
Si Non : construis directement docs/design-spec.md avec le module comme base, sans t'arrêter.
```
**F. Audit de sécurité** :
```
Suis agent-protocol, references/audit-securite.md. Lis toute la codebase avant conclusion,
verdict individuel par item de checklist, format de conclusion imposé, rapport final avec posture globale.
```
**G. Entrée unique — projet complet** :
```
Suis la compétence agent-protocol.
1. Détermine {{TYPE_PROJET}}, remplis la fiche YAML (section 1).
2. Consulte le Router (section 5) pour les skills/modules par jalon.
3. Exécute A→F : brief · plan · architecture (si complexité) ·
   design → au Jalon D, pose d'abord la question de confirmation Claude Design ; si Oui, produis
   docs/handoff-claude-design.md et ARRÊTE-TOI jusqu'au retour ; si Non, fais le design directement ·
   construction (+ directives/execution si sous-tâche récurrente) · tests/déploiement (+ audit sécurité si SaaS/DB/auth).
4. ≤ 3 questions avant chaque jalon si info manquante, valide avant de passer au suivant.
5. Ne relis pas un skill déjà chargé. Signale tout skill/module absent du Router.
Description : {{DESCRIPTION_IDEE}} | Type pressenti : {{TYPE_PROJET}}
```

---

## 11. Règle de Décision Finale

En cas de conflit entre objectifs :
**Sécurité & exactitude > Instructions locales du dépôt > Maintenabilité > Vitesse > Embellissement**
> Toute affirmation de succès doit être appuyée par une commande, un test ou un scénario effectivement exécuté.

---

## 12. Checklist Finale (contrôle qualité & tokens)

- [ ] README + AGENTS.md + état Git lus avant toute action
- [ ] Découverte des skills effectuée une seule fois — registre de session rempli
- [ ] Fiche YAML (section 1) complétée ou fiche d'hypothèses produite
- [ ] `execution/` vérifié avant l'écriture de tout nouveau script déterministe
- [ ] Chaque jalon a produit un fichier `docs/` court et daté
- [ ] Architecture proportionnée à la taille réelle du projet
- [ ] **Jalon D** : question de confirmation Claude Design posée systématiquement ; si Oui → `docs/handoff-claude-design.md` produit, session arrêtée, retour reçu et consigné dans `docs/design-spec.md` avant tout code ; si Non → `docs/design-spec.md` produit directement avec les skills internes
- [ ] Chaque lot de construction testé avant le suivant
- [ ] Qualité non négociable vérifiée à chaque lot (validation serveur, états UI, a11y, pas de secrets)
- [ ] `docs/decisions.md` reflète tous les choix figés ; `directives/` mises à jour si apprentissage sur tâche récurrente
- [ ] `accidental-data-loss-prevention` activé avant toute opération destructive
- [ ] Core Web Vitals vérifiés · Accessibilité WCAG AA auditée
- [ ] Audit sécurité exécuté si SaaS/Fullstack/Auth/DB (`references/audit-securite.md`)
- [ ] Rapport de livraison `docs/audit.md` produit
- [ ] Aucun secret dans Git — `.env.example` documenté

---

## 13. Index Rapide — Skills/Modules par Jalon

| Jalon | Essentiels | Optionnels |
|---|---|---|
| **A · Cadrage** | `brainstorming` | `ui-ux-pro-max` `planification` |
| **B · Plan** | `planification` | `doc-coauthoring` `slides` |
| **C · Architecture** | `doc-coauthoring` | `managing-python-dependencies` skill DB dédié |
| **D · Design** | **Claude Design** — voie par défaut, confirmée par question explicite | `saas-designer` `landing-cinematique` `cv-cinematique` `ui-ux-pro-max` `design-system` `frontend-design` `brand` `canvas-design` `stitch` — intrants si Oui, exécutés directement si Non |
| **E · Construction** | `modern-web-guidance` + Router | `web-artifacts-builder` `claude-api` `mcp-builder` `google-antigravity-sdk` couche `directives/`+`execution/` |
| **F · Tests/Deploy** | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` | `memory-leak-debugging` `chrome-devtools` audit sécurité |

---

*Protocole POSER v4.0 · fusion AGENTS.md (couches Directive/Orchestration/Exécution) + POSER v3 (jalons A→F) + modules izisaas (landing/CV cinématographiques, SaaS Designer, audit sécurité) · Compatible Claude Code & Antigravity (Gemini)*
