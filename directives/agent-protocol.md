# AGENT-PROTOCOL.md
### Protocole POSER — Pilotage économe en tokens · Antigravity / Claude Code

> **À placer à la racine de chaque projet** (aux côtés de `CLAUDE.md` / `AGENTS.md`).
> Ce fichier est le **chef d'orchestre**. Il indique à l'agent QUAND lire quoi,
> QUELLES compétences mobiliser à chaque phase, et COMMENT ne pas relire deux fois la même chose.
> Il ne remplace pas les skills eux-mêmes : il leur sert de **routeur**.
>
> **Dossier de skills système** : `~/.gemini/config/skills/` (93 compétences disponibles)

---

## 0. Règles globales d'économie de tokens (à respecter à CHAQUE phase)

1. **Scanner avant d'agir** : au début de chaque phase, l'agent liste le dossier de skills disponibles (`ls ~/.gemini/config/skills/`) et ne lit **que** les `SKILL.md` dont la description correspond à la phase en cours. Ne jamais relire un skill déjà chargé dans la session.
2. **Une seule source de vérité** : les décisions validées (stack, palette, architecture) sont écrites dans `/docs/decisions.md` au fur et à mesure. L'agent lit ce fichier plutôt que de redemander le contexte à l'utilisateur.
3. **Pas de sur-planification** : la profondeur du plan doit être proportionnelle à la taille du projet (une landing page ne nécessite pas un ADR de 10 pages).
4. **Livrables incrémentaux** : chaque phase produit un fichier court et daté dans `/docs/` plutôt qu'un pavé unique en fin de projet.
5. **Confirmation avant exécution lourde** : avant `build`, `deploy`, ou toute action irréversible, l'agent résume en 5 lignes ce qu'il va faire et attend un feu vert.
6. **Skills manquants** : si un skill listé n'existe pas dans `~/.gemini/config/skills/`, le signaler à l'utilisateur au lieu d'improviser silencieusement.

---

## 1. Référentiel des Skills Disponibles par Famille

> L'agent consulte ce référentiel pour identifier rapidement les skills à mobiliser.
> Chemin absolu : `~/.gemini/config/skills/<nom-du-skill>/SKILL.md`

### 🧠 Stratégie & Workflow
| Skill | Usage |
|-------|-------|
| `brainstorming` | Exploration de besoins avant toute implémentation |
| `planification` | Plans d'implémentation multi-étapes avec TDD |
| `skill-creator` | Créer ou améliorer des compétences |
| `skill-repair` | Réparer des skills cassés |
| `accidental-data-loss-prevention` | Confirmation avant toute opération destructive |

### 🎨 Design & UI/UX
| Skill | Usage |
|-------|-------|
| `stitch` | Génération de maquettes UI via Stitch MCP (screens, design system) |
| `ui-ux-pro-max` | Recommandations UX, patterns, palettes, typographies (84 styles) |
| `design` | Identité visuelle complète (logo, CIP, mockups) |
| `design-system` | Tokens de design (couleurs, typo, espacement, composants) |
| `frontend-design` | Direction visuelle intentionnelle pour le frontend |
| `brand` | Identité de marque, brand voice, messaging |
| `brand-guidelines` | Application de la charte graphique Anthropic |
| `canvas-design` | Visuels statiques (posters, hero images, affiches) |
| `banner-design` | Bannières réseaux sociaux et publicités |
| `theme-factory` | Application rapide d'un thème cohérent |
| `ui-styling` | Composants shadcn/ui + Tailwind |
| `algorithmic-art` | Art génératif p5.js, flow fields, animations |

### 💻 Développement Web & Frontend
| Skill | Usage |
|-------|-------|
| `modern-web-guidance` | Bonnes pratiques web modernes (HTML/CSS/JS, APIs) |
| `web-artifacts-builder` | Artefacts React complexes (shadcn/ui, routing, state) |
| `frontend-design` | Design frontend distinctif et intentionnel |
| `chrome-extensions` | Extensions Chrome Manifest V3 |
| `mcp-builder` | Création de serveurs MCP |
| `claude-api` | Intégration API Anthropic/Claude (streaming, tools, agents) |
| `google-antigravity-sdk` | Agents multi-agents avec le SDK Antigravity |
| `android-cli` | Développement Android CLI |

### 🧪 Tests & Débogage
| Skill | Usage |
|-------|-------|
| `webapp-testing` | Tests fonctionnels via Playwright (UI, formulaires, navigation) |
| `a11y-debugging` | Audit accessibilité (ARIA, contraste, clavier, tap targets) |
| `debug-optimize-lcp` | Optimisation Core Web Vitals (LCP, CLS, INP) |
| `memory-leak-debugging` | Détection fuites mémoire JS/Node.js |
| `chrome-devtools` | Débogage et automation navigateur via DevTools MCP |
| `troubleshooting` | Dépannage connexion DevTools |

### 📄 Documents & Présentations
| Skill | Usage |
|-------|-------|
| `slides` | Présentations HTML avec Chart.js |
| `doc-coauthoring` | Co-rédaction de documentation structurée |
| `docx` | Fichiers Word .docx |
| `pdf` | Manipulation et création de PDFs |
| `pptx` | Présentations PowerPoint .pptx |
| `xlsx` | Tableurs Excel .xlsx |
| `internal-comms` | Communications internes (rapports, newsletters) |

### 🎬 Médias & Créatif
| Skill | Usage |
|-------|-------|
| `remotion-best-practices` | Vidéos animées React (Remotion) |
| `slack-gif-creator` | GIFs animés optimisés Slack |

### ☁️ Google Cloud Platform & Data
| Skill | Usage |
|-------|-------|
| `bigquery` | Requêtes SQL BigQuery, optimisation, ML |
| `building-data-apps` | Dashboards data (React + Recharts ou Streamlit) |
| `data-autocleaning` | Nettoyage automatique de données |
| `dataform-bigquery` | Pipelines ELT Dataform |
| `dbt-bigquery` | Pipelines dbt pour BigQuery |
| `firestore-data` | Opérations CRUD Firestore NoSQL |
| `gcp-data-pipelines` | Orchestration de pipelines data GCP |
| `gcp-dataflow` | Pipelines Apache Beam / Dataflow |
| `gcp-pipeline-orchestration` | Orchestration Cloud Composer |
| `gcp-spark` | Spark sur Dataproc |
| `ml-best-practices` | Machine learning (classification, régression, clustering) |
| `notebook-guidance` | Notebooks Jupyter + BigQuery magics |
| `discovering-gcp-data-assets` | Exploration de datasets GCP |
| `managing-python-dependencies` | Gestion venv, pip, uv — scripts Python |
| `gcloud-auth-verification` | Authentification Google Cloud ADC |
| `gcs-security-assessment` | Audit sécurité GCS |

### 🛢️ Bases de Données (AlloyDB & Cloud SQL)
`alloydb-omni-*` (9 skills) · `alloydb-postgres-*` (7 skills) · `cloud-sql-mysql-*` (4) · `cloud-sql-postgres-*` (8) · `cloud-sql-sqlserver-*` (4) · `spanner-data`

---

## 2. Le Router de Projet

L'agent commence **toujours** par déterminer `{{TYPE_PROJET}}` puis consulte la ligne correspondante.

| Type de projet | Skills Phase 1 (Brainstorm) | Skills Phase 3 (Design) | Skills Phase 4 (Dev) | Skills Phase 5 (Tests) | Complexité archi. |
|---|---|---|---|---|---|
| **Automatisation tâche/processus** | `brainstorming` `planification` | _(aucun)_ | `managing-python-dependencies` `accidental-data-loss-prevention` | _(tests manuels)_ | Faible — pipeline linéaire |
| **SaaS** | `brainstorming` `planification` `ui-ux-pro-max` | `stitch` `design-system` `brand` `frontend-design` | `modern-web-guidance` `web-artifacts-builder` `claude-api` | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` | Élevée — multi-services |
| **Landing page** | `brainstorming` `ui-ux-pro-max` | `stitch` `frontend-design` `brand` `canvas-design` `banner-design` | `modern-web-guidance` | `a11y-debugging` `debug-optimize-lcp` | Très faible |
| **Dashboard / Data** | `brainstorming` `planification` | `stitch` `ui-ux-pro-max` `design-system` | `building-data-apps` `modern-web-guidance` | `webapp-testing` `debug-optimize-lcp` | Moyenne |
| **Jeu navigateur** | `brainstorming` `planification` | `frontend-design` `algorithmic-art` `canvas-design` | `modern-web-guidance` `web-artifacts-builder` | `webapp-testing` `chrome-devtools` | Moyenne |
| **Design → Code (image uploadée)** | `brainstorming` `ui-ux-pro-max` | `stitch` `frontend-design` `design-system` | `modern-web-guidance` `web-artifacts-builder` | `a11y-debugging` `debug-optimize-lcp` | Faible à moyenne |
| **Application fullstack** | `brainstorming` `planification` `ui-ux-pro-max` | `stitch` `design-system` `brand` `frontend-design` | `modern-web-guidance` `web-artifacts-builder` `claude-api` `managing-python-dependencies` | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` `memory-leak-debugging` | Élevée |
| **Boutique en ligne** | `brainstorming` `planification` `ui-ux-pro-max` | `stitch` `design-system` `brand` `frontend-design` `canvas-design` | `modern-web-guidance` `web-artifacts-builder` | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` | Moyenne à élevée |
| **Site web (vitrine)** | `brainstorming` `ui-ux-pro-max` | `stitch` `frontend-design` `brand` `canvas-design` | `modern-web-guidance` | `a11y-debugging` `debug-optimize-lcp` | Faible à moyenne |
| **Vidéo / Motion** | `brainstorming` | `design-system` `canvas-design` | `remotion-best-practices` | _(validation manuelle)_ | Faible |
| **Agent IA / MCP** | `brainstorming` `planification` | _(aucun)_ | `claude-api` `mcp-builder` `google-antigravity-sdk` `managing-python-dependencies` | `webapp-testing` | Élevée |
| **Data Pipeline GCP** | `brainstorming` `planification` | _(aucun)_ | `gcp-data-pipelines` `managing-python-dependencies` `bigquery` | `gcp-pipeline-orchestration` | Élevée |

---

## 3. Phase 1 — Brainstorming & Cadrage

**But** : transformer une idée floue en un brief exploitable, sans coder.

**Skills à mobiliser** : `brainstorming` · `ui-ux-pro-max` (si projet UI) · `planification` (pour pré-cadrer la portée)

```
[PERSONA]
Agis en tant que consultant produit senior, à la fois créatif et pragmatique,
habitué à cadrer des projets {{TYPE_PROJET}} pour des porteurs de projet non-techniques.

[OBJECTIF]
Aide-moi à clarifier l'idée suivante : {{DESCRIPTION_IDEE}}.
Le but final est de produire un brief clair qui servira de base au plan de construction,
afin d'éviter les allers-retours coûteux en tokens plus tard dans le projet.

[SITUATION]
- Type de projet : {{TYPE_PROJET}}
- Public cible : {{PUBLIC_CIBLE}}
- Contraintes connues : {{CONTRAINTES}} (budget de temps, stack imposée, délai…)
- Ressources déjà disponibles : {{FICHIERS_OU_LIENS}}

[SKILLS À ACTIVER]
1. Commence par lire `~/.gemini/config/skills/brainstorming/SKILL.md`
2. Si le projet a une composante UI : lis aussi `~/.gemini/config/skills/ui-ux-pro-max/SKILL.md`
   pour proposer 2-3 directions visuelles après le cadrage fonctionnel.

[EXCLUSIONS]
Ne commence PAS à écrire de code ni à choisir une stack technique à ce stade.
Reste au niveau du besoin, des fonctionnalités et de l'expérience utilisateur.
N'invente pas de contraintes non données ; liste-les comme hypothèses à valider.

[BONUS — ITÉRATION]
Avant de produire le brief final, pose-moi 5 questions maximum pour combler les zones
d'ombre (fonctionnalités indispensables vs. secondaires, ton/style, échéance, budget technique).
```

**Sortie attendue** : `/docs/01-brief.md` (1 page max).

---

## 4. Phase 2 — Plan de Construction

**But** : découper le brief en tâches ordonnées, avec jalons vérifiables.

**Skills à mobiliser** : `planification` · `doc-coauthoring` · `slides` (si présentation stakeholders)

```
[PERSONA]
Agis en tant que chef de projet technique rigoureux, spécialisé dans les livraisons
itératives de projets {{TYPE_PROJET}}.

[OBJECTIF]
À partir de /docs/01-brief.md, produis un plan de construction en jalons (milestones),
afin de valider l'avancement étape par étape et éviter un développement monolithique
qui gaspillerait des tokens en cas d'erreur tardive.

[SITUATION]
Consulte d'abord /docs/decisions.md s'il existe.
Consulte la colonne Skills du Router de Projet (section 2) pour {{TYPE_PROJET}}.

[SKILLS À ACTIVER]
1. Lis `~/.gemini/config/skills/planification/SKILL.md` — applique son format de plan TDD.
2. Pour chaque jalon, indique explicitement : skill mobilisé · commande de test · critère de "terminé".

[EXCLUSIONS]
Ne détaille pas le code ligne par ligne à ce stade. Découpe en tâches atomiques
(1 tâche = 1 commit testable), avec critère de "terminé" explicite.
Ne planifie pas plus de granularité que nécessaire pour ce type de projet.

[FORMAT ATTENDU]
Pour chaque jalon :
- Objectif
- Tâches (liste à puces)
- Skill mobilisé (`nom-du-skill`)
- Critère de validation (commande ou vérification manuelle)

[BONUS — ITÉRATION]
Propose le plan, puis demande validation ou ajustement avant de continuer.
```

**Sortie attendue** : `/docs/02-plan.md`.

---

## 5. Phase 3 — Document d'Architecture

**But** : figer les choix techniques structurants (uniquement si le projet le justifie — cf. colonne "Complexité archi." du Router).

**Skills à mobiliser** : `doc-coauthoring` · `managing-python-dependencies` (si back Python) · `gcloud-auth-verification` (si GCP)

```
[PERSONA]
Agis en tant qu'architecte logiciel senior, orienté simplicité et maintenabilité,
qui refuse la sur-ingénierie.

[OBJECTIF]
Rédige un document d'architecture (ADR léger) pour {{TYPE_PROJET}}, afin de figer
la stack, les flux de données et les intégrations avant toute ligne de code.

[SITUATION]
Base-toi sur /docs/01-brief.md et /docs/02-plan.md.
Contraintes techniques connues : {{STACK_IMPOSEE_OU_PREFERENCES}}.

[SKILLS À ACTIVER]
- Si backend Python → `managing-python-dependencies` (conventions de dépendances)
- Si déploiement GCP → `gcloud-auth-verification` + skills GCP correspondants
- Si base de données → consulte le skill `cloud-sql-postgres-admin` ou `firestore-data` selon le choix

[EXCLUSIONS]
N'ajoute pas de composants non justifiés par le brief (pas de microservices pour une
landing page, pas de base de données pour un site vitrine statique).
Justifie chaque choix en une phrase.

[FORMAT ATTENDU]
Contexte / Stack retenue (front, back, data, hébergement) /
Schéma des flux (texte ou mermaid) / Alternatives écartées et pourquoi.

[BONUS — ITÉRATION]
Si plusieurs stacks sont plausibles, présente-les en tableau comparatif et demande
de trancher avant de rédiger la version finale.
```

**Sortie attendue** : `/docs/03-architecture.md` (+ schéma Mermaid si utile).
**Note token** : pour une landing page ou un site simple, cette phase peut être **fusionnée en 3 lignes** dans le plan.

---

## 6. Phase 4 — Design

**But** : définir l'identité visuelle et les composants avant le développement.

**Skills à mobiliser** (selon type de projet) :

| Besoin | Skill à activer |
|--------|----------------|
| Maquettes UI écrans complets | `stitch` |
| Palette · typo · patterns UX | `ui-ux-pro-max` |
| Design system (tokens CSS) | `design-system` |
| Direction visuelle frontend | `frontend-design` |
| Identité de marque + copy | `brand` |
| Thème rapide cohérent | `theme-factory` |
| Visuels statiques (hero, OG) | `canvas-design` |
| Bannières réseaux sociaux | `banner-design` |
| Composants shadcn/Tailwind | `ui-styling` |
| Art génératif / jeu | `algorithmic-art` |

```
[PERSONA]
Agis en tant que designer produit senior, avec un sens aigu de l'esthétique moderne
et de la cohérence de design system.

[OBJECTIF]
Propose une direction visuelle pour {{TYPE_PROJET}}, afin de guider la construction
front-end sans avoir à retoucher le style après coup.

[SITUATION]
- Ton/ambiance souhaité(e) : {{TON_VISUEL}} (épuré, ludique, corporate, glassmorphism…)
- Référence visuelle fournie (si applicable) : {{IMAGE_OU_LIEN}}

[SKILLS À ACTIVER — dans cet ordre]
1. `stitch` → générer les maquettes écrans clés (desktop + mobile) via StitchMCP
2. `ui-ux-pro-max` → valider les choix UX, patterns, et palettes de couleurs
3. `design-system` → produire les tokens CSS (variables, espacement, typographie)
4. `frontend-design` → direction visuelle intentionnelle (pas de "template générique")
5. `brand` → si le projet nécessite une identité de marque complète
6. `canvas-design` → visuels hero image, Open Graph, favicon
7. `banner-design` → bannières LinkedIn, Twitter/X si besoin marketing

[EXCLUSIONS]
N'utilise pas de composants par défaut génériques ("template Bootstrap-like").
Propose une palette, une typographie et une hiérarchie visuelle intentionnelles.

[FORMAT ATTENDU]
Donne 2 directions distinctes :
- Direction A : [style] — palette · typo · exemple composant clé
- Direction B : [style] — palette · typo · exemple composant clé

[BONUS — ITÉRATION]
Demande de choisir une direction (ou de fusionner des éléments) avant de générer
les maquettes/composants définitifs.
```

**Sortie attendue** : `/docs/04-design.md` + maquettes Stitch + tokens CSS.

---

## 7. Phase 5 — Construction & Exécution

**But** : coder, tester, livrer — en suivant strictement le plan et l'architecture validés.

**Skills à mobiliser** (selon type de projet) :

| Besoin | Skill à activer |
|--------|----------------|
| Frontend moderne (HTML/CSS/JS) | `modern-web-guidance` |
| Composants React complexes | `web-artifacts-builder` |
| Extension Chrome | `chrome-extensions` |
| Intégration Claude / Gemini | `claude-api` |
| Agent IA multi-composants | `google-antigravity-sdk` |
| Serveur MCP custom | `mcp-builder` |
| Scripts Python + dépendances | `managing-python-dependencies` |
| Dashboard data | `building-data-apps` |
| Pipeline GCP | `gcp-data-pipelines` `gcp-pipeline-orchestration` |
| Données BigQuery | `bigquery` |
| Base de données Cloud SQL | `cloud-sql-postgres-admin` `cloud-sql-postgres-data` |
| Base de données Firestore | `firestore-data` |
| Vidéo React (Remotion) | `remotion-best-practices` |
| Opération destructive (DELETE) | `accidental-data-loss-prevention` ← **OBLIGATOIRE** |

```
[PERSONA]
Agis en tant que développeur senior full-stack, discipliné, qui livre par petites
itérations testables plutôt que par gros blocs.

[OBJECTIF]
Implémente le jalon {{NUMERO_JALON}} du plan (/docs/02-plan.md), en respectant
l'architecture (/docs/03-architecture.md) et le design (/docs/04-design.md),
afin de produire un incrément fonctionnel et vérifiable.

[SITUATION]
Type de projet : {{TYPE_PROJET}}.

[SKILLS À ACTIVER — dans cet ordre]
1. Identifie les skills de construction dans le Router (section 2) pour {{TYPE_PROJET}}
2. Pour chaque skill listé, vérifie qu'il existe dans `~/.gemini/config/skills/`
3. Si skill manquant → signale-le avant de commencer, ne pas improviser

[SÉQUENCE DE CONSTRUCTION]
Pour chaque tâche du jalon :
a) Écrire le test qui échoue (TDD)
b) Implémenter le minimum pour faire passer le test
c) Vérifier le test → commit
d) Documenter dans /docs/05-changelog.md

[EXCLUSIONS]
Ne touche pas aux fichiers/jalons hors du périmètre de cette tâche.
Ne réécris pas l'architecture ou le design déjà validés.
Si un blocage impose une modification → signale-le, propose, attends validation.

[AVANT TOUTE ACTION DESTRUCTIVE]
Activer `accidental-data-loss-prevention` → résumer en 5 lignes + attendre feu vert.

[BONUS — ITÉRATION]
À la fin du jalon, fournis un résumé de 5 lignes :
- Ce qui a été fait
- Comment tester
- Ce qui reste
Avant de passer au jalon suivant.
```

**Sortie attendue** : code + `/docs/05-changelog.md` mis à jour à chaque jalon.

---

## 8. Phase 6 — Tests, Audit & Déploiement

**But** : valider la qualité, corriger, déployer.

**Skills à mobiliser** :

| Besoin | Skill à activer |
|--------|----------------|
| Tests fonctionnels (Playwright) | `webapp-testing` |
| Audit accessibilité (WCAG) | `a11y-debugging` |
| Optimisation Core Web Vitals | `debug-optimize-lcp` |
| Fuites mémoire JS | `memory-leak-debugging` |
| Débogage navigateur DevTools | `chrome-devtools` |
| Dépannage connexion | `troubleshooting` |

```
[PERSONA]
Agis en tant qu'ingénieur QA senior et expert performance web.

[OBJECTIF]
Valide la qualité de l'application {{NOM_PROJET}} avant mise en production,
en couvrant fonctionnel, accessibilité, performance et déploiement.

[SKILLS À ACTIVER — dans cet ordre]
1. `webapp-testing` → tests fonctionnels (scénarios utilisateur, mobile + desktop)
2. `a11y-debugging` → audit WCAG AA (structure HTML, ARIA, contraste, clavier)
3. `debug-optimize-lcp` → Core Web Vitals (LCP < 2.5s, CLS < 0.1, INP < 200ms)
4. `memory-leak-debugging` → si l'app a une longue session ou état complexe
5. `chrome-devtools` → inspection réseau, console, profiling si problème persistant

[SÉQUENCE]
a) Tests fonctionnels → rapport de bugs
b) Corriger les bugs bloquants
c) Audit accessibilité → rapport
d) Corriger les issues de sévérité haute
e) Audit performance → actions correctives
f) Déploiement (résumé 5 lignes + validation avant lancement)

[AVANT DÉPLOIEMENT]
Résumer : commande de build · variables d'env · domaine · provider.
Attendre validation explicite avant d'exécuter.
```

**Sortie attendue** : `/docs/06-audit.md` + app déployée.

---

## 9. Le Prompt d'Entrée Unique (à coller dans Antigravity / Claude Code)

```
Tu vas suivre le fichier AGENT-PROTOCOL.md présent à la racine du projet.
Les skills disponibles sont dans `~/.gemini/config/skills/` (93 compétences).

1. Détermine {{TYPE_PROJET}} à partir de ma description ci-dessous.
2. Consulte le Router de Projet (section 2) pour identifier les skills à mobiliser par phase.
3. Exécute les phases dans l'ordre :
   Phase 1 : Brainstorming → /docs/01-brief.md
   Phase 2 : Plan          → /docs/02-plan.md
   Phase 3 : Architecture  → /docs/03-architecture.md (si complexité le justifie)
   Phase 4 : Design        → /docs/04-design.md + maquettes Stitch
   Phase 5 : Construction  → code + /docs/05-changelog.md
   Phase 6 : Tests/Deploy  → /docs/06-audit.md
4. Avant chaque phase : pose jusqu'à 5 questions si des informations manquent,
   puis attends ma validation avant de passer à la phase suivante.
5. Ne relis pas un skill déjà chargé dans cette session.
6. Si un skill du Router n'existe pas dans ~/.gemini/config/skills/, signale-le.

Description du projet : {{DESCRIPTION_IDEE}}
Type pressenti : {{TYPE_PROJET}}
(landing page / dashboard / SaaS / jeu / design-to-code / app fullstack /
 boutique / site web / automatisation / agent IA / data pipeline)
```

---

## 10. Checklist Finale (contrôle qualité & tokens)

- [ ] Chaque phase a produit un fichier `/docs/0X-*.md` court et daté
- [ ] Aucun skill n'a été relu deux fois inutilement dans la session
- [ ] L'architecture est proportionnée à la taille réelle du projet
- [ ] Le design (`stitch` + `design-system`) a été validé **avant** le début du code
- [ ] Chaque jalon de construction a été testé avant de passer au suivant
- [ ] `/docs/decisions.md` reflète tous les choix figés (source de vérité unique)
- [ ] `accidental-data-loss-prevention` activé avant toute opération destructive
- [ ] Les métriques Core Web Vitals ont été vérifiées (`debug-optimize-lcp`)
- [ ] L'accessibilité WCAG AA a été auditée (`a11y-debugging`)

---

## 11. Index Rapide — Skills par Phase

| Phase | Skills essentiels | Skills optionnels |
|-------|------------------|------------------|
| **1 · Brainstorming** | `brainstorming` | `ui-ux-pro-max` `planification` |
| **2 · Plan** | `planification` | `doc-coauthoring` `slides` |
| **3 · Architecture** | `doc-coauthoring` | `managing-python-dependencies` `gcloud-auth-verification` |
| **4 · Design** | `stitch` `design-system` `frontend-design` | `ui-ux-pro-max` `brand` `canvas-design` `banner-design` `theme-factory` `ui-styling` `algorithmic-art` |
| **5 · Construction** | `modern-web-guidance` + skills spécifiques projet | `web-artifacts-builder` `claude-api` `mcp-builder` `google-antigravity-sdk` `managing-python-dependencies` `building-data-apps` `remotion-best-practices` |
| **6 · Tests/Deploy** | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` | `memory-leak-debugging` `chrome-devtools` `troubleshooting` |

---

*Protocole POSER v2.0 · 2026-07-20 · Compatible Antigravity (Gemini) & Claude Code*
*Skills disponibles : 93 · Dossier : `~/.gemini/config/skills/`*
*Dupliquer par projet et remplir les `{{VARIABLES}}`.*
