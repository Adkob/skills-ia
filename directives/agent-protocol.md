# AGENT-PROTOCOL.md
### Protocole POSER v3 — Pilotage économe en tokens · Antigravity / Claude Code

> **À placer à la racine de chaque projet** (aux côtés de `CLAUDE.md` / `AGENTS.md`).
> **But** : livrer un projet fiable en minimisant les appels, le contexte chargé et les modifications inutiles.
> Ce fichier est le **chef d'orchestre** : il indique à l'agent QUAND lire quoi,
> QUELLES compétences mobiliser à chaque phase, et COMMENT ne pas relire deux fois la même chose.
>
> **Règle d'adaptation** : ce dépôt est la source de vérité. Les skills installés globalement
> ne sont utilisés qu'après une découverte courte et ciblée. Ne jamais inventer un outil,
> une commande ou une intégration.
>
> **Dossier de skills système** : `~/.gemini/config/skills/` (93 compétences disponibles)

---

## 0. Contrat opérationnel (à respecter à CHAQUE tâche)

1. **Lire avant d'écrire.** Examiner d'abord `README*`, la configuration du projet, les instructions locales (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, etc.) et l'état Git (`git status`, `git log --oneline -5`). Ne pas lire récursivement tout le dépôt.
2. **Découvrir les capacités une seule fois par session.** Identifier uniquement les skills pertinents pour l'objectif. Lire leur `SKILL.md` (nom, description, prérequis, outils exposés, limites), pas leur code source complet, sauf blocage.
3. **Sélectionner peu d'outils.** Maximum 1–3 skills complémentaires par étape. Privilégier les outils natifs et les dépendances déjà présentes.
4. **Scanner avant d'agir** : lister `ls ~/.gemini/config/skills/` et ne lire que les `SKILL.md` correspondant à la phase. Ne jamais relire un skill déjà chargé dans la session.
5. **Travailler par jalons.** Ne passer au jalon suivant qu'après le critère de sortie correspondant. Demander validation humaine uniquement pour les décisions irréversibles, coûteuses ou ambiguës.
6. **Faire des changements atomiques.** Petits lots cohérents, formatage, tests ciblés, vérification du résultat. Ne pas refactoriser hors périmètre.
7. **Ne jamais exposer de secrets.** Ne pas afficher ni inscrire les valeurs de `.env`, clés API ou identifiants. Utiliser `.env.example` et les mécanismes sécurisés existants.
8. **Rendre compte brièvement.** Après un jalon : faits, fichiers modifiés, validation exécutée, risques/décision attendue — pas de journal exhaustif.
9. **Une seule source de vérité** : les décisions validées sont écrites dans `/docs/decisions.md`. L'agent lit ce fichier plutôt que de redemander le contexte ou de le régénérer.
10. **Skills manquants** : si un skill listé n'existe pas dans `~/.gemini/config/skills/`, le signaler à l'utilisateur au lieu d'improviser silencieusement.

### Budget de contexte

- Commencer par un **résumé opérationnel ≤ 250 mots**.
- Préférer les chemins, extraits ciblés et résultats synthétiques aux gros dumps.
- Pour toute documentation, générer un squelette puis remplir seulement les rubriques affectées.
- Si l'incertitude bloque une décision structurante, poser **au plus 3 questions regroupées**. Sinon, annoncer une hypothèse réversible et avancer.
- **Pas de sur-planification** : la profondeur du plan doit être proportionnelle à la taille du projet (une landing page ne nécessite pas un ADR de 10 pages).

---

## 1. Entrée Projet — Remplir ou Inférer avec Prudence

```yaml
projet:
  type: automation | saas | landing-page | dashboard | jeu-navigateur | design-to-code | fullstack | storefront | site-web | video-motion | agent-ia | data-pipeline | autre
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

> Si ces informations ne sont pas disponibles, produire une **fiche d'hypothèses** (≤ 8 lignes) et demander uniquement celles dont l'absence empêche de démarrer.

---

## 2. Référentiel des Skills Disponibles par Famille

> Chemin absolu : `~/.gemini/config/skills/<nom-du-skill>/SKILL.md`
> L'agent consulte ce référentiel pour identifier les skills à mobiliser — ne jamais inventer un skill absent.

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

## 3. Découverte Ciblée des Skills (procédure obligatoire, courte)

Effectuer une fois par session, pas à chaque tâche.

1. Lire `README*`, `AGENTS.md`, `CLAUDE.md` et `git log --oneline -5`.
2. Rechercher par intention parmi les skills : `brainstorm`, `planning`, `architecture`, `ui`, `frontend`, `design`, `database`, `auth`, `testing`, `e2e`, `deploy`, `security`, `browser`, `automation`, `workflow`, `mcp`.
3. Pour chaque candidat, lire uniquement : nom, description, prérequis, outils exposés, limites.
4. Choisir les capacités qui améliorent réellement ce projet ; justifier la sélection en une ligne.

**Registre de session** (ne pas répéter si inchangé) :

```md
## Capacités retenues
| Jalon | Skill | Usage précis | Pourquoi |
|-------|-------|-------------|---------|
| cadrage | brainstorming | exploration du besoin | requis avant toute implémentation |
| design | stitch | maquettes écrans | génération visuelle MCP |
| construction | … | … | … |
| validation | … | … | … |
```

**Interdits** : installer un plugin/dépendance, appeler un service payant, accéder à une intégration externe ou lancer un déploiement sans consentement explicite. En cas d'absence de skill approprié, poursuivre avec les outils standards.

---

## 4. Le Router de Projet

L'agent commence **toujours** par déterminer `{{TYPE_PROJET}}` puis consulte cette table.

| Type de projet | Priorité | Skills Jalon A-B | Skills Jalon D (Design) | Skills Jalon E (Dev) | Skills Jalon F (Tests) | Complexité archi. |
|---|---|---|---|---|---|---|
| **Automatisation** | fiabilité, idempotence, observabilité | `brainstorming` `planification` | _(aucun)_ | `managing-python-dependencies` `accidental-data-loss-prevention` | _(tests manuels + retry)_ | Faible |
| **SaaS** | domaine, auth, données, tests | `brainstorming` `planification` `ui-ux-pro-max` | `stitch` `design-system` `brand` `frontend-design` | `modern-web-guidance` `web-artifacts-builder` `claude-api` | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` | Élevée |
| **Landing page** | conversion, design, vitesse | `brainstorming` `ui-ux-pro-max` | `stitch` `frontend-design` `brand` `canvas-design` `banner-design` | `modern-web-guidance` | `a11y-debugging` `debug-optimize-lcp` | Très faible |
| **Dashboard / Data** | justesse et lecture des données | `brainstorming` `planification` | `stitch` `ui-ux-pro-max` `design-system` | `building-data-apps` `modern-web-guidance` | `webapp-testing` `debug-optimize-lcp` | Moyenne |
| **Jeu navigateur** | boucle jouable, réactivité | `brainstorming` `planification` | `frontend-design` `algorithmic-art` `canvas-design` | `modern-web-guidance` `web-artifacts-builder` | `webapp-testing` `chrome-devtools` | Moyenne |
| **Design → Code** | fidélité, responsive, a11y | `brainstorming` `ui-ux-pro-max` | `stitch` `frontend-design` `design-system` | `modern-web-guidance` `web-artifacts-builder` | `a11y-debugging` `debug-optimize-lcp` | Faible à moyenne |
| **Fullstack** | domaine, auth, données, E2E | `brainstorming` `planification` `ui-ux-pro-max` | `stitch` `design-system` `brand` `frontend-design` | `modern-web-guidance` `web-artifacts-builder` `claude-api` `managing-python-dependencies` | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` `memory-leak-debugging` | Élevée |
| **Storefront** | parcours d'achat sûr | `brainstorming` `planification` `ui-ux-pro-max` | `stitch` `design-system` `brand` `frontend-design` `canvas-design` | `modern-web-guidance` `web-artifacts-builder` | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` | Moyenne à élevée |
| **Site web (vitrine)** | design, SEO, vitesse | `brainstorming` `ui-ux-pro-max` | `stitch` `frontend-design` `brand` `canvas-design` | `modern-web-guidance` | `a11y-debugging` `debug-optimize-lcp` | Faible à moyenne |
| **Vidéo / Motion** | fluidité, rendu | `brainstorming` | `design-system` `canvas-design` | `remotion-best-practices` | _(validation manuelle)_ | Faible |
| **Agent IA / MCP** | fiabilité, sécurité, tests | `brainstorming` `planification` | _(aucun)_ | `claude-api` `mcp-builder` `google-antigravity-sdk` `managing-python-dependencies` | `webapp-testing` | Élevée |
| **Data Pipeline GCP** | correctness, idempotence | `brainstorming` `planification` | _(aucun)_ | `gcp-data-pipelines` `managing-python-dependencies` `bigquery` | `gcp-pipeline-orchestration` | Élevée |

---

## 5. Pipeline à Jalons (A → F)

### Jalon A — Cadrage, Brainstorming & Brief

**But** : transformer la demande en MVP testable, sans construire.
**Skills** : `brainstorming` · `ui-ux-pro-max` (si projet UI) · `planification` (pré-cadrage portée)

```
[PERSONA] Consultant produit senior, créatif et pragmatique.

[OBJECTIF] Clarifier : {{DESCRIPTION_IDEE}}
Produire un brief exploitable pour éviter les allers-retours coûteux en tokens.

[SITUATION]
- Type : {{TYPE_PROJET}} | Cible : {{PUBLIC_CIBLE}}
- Contraintes : {{CONTRAINTES}} | Ressources : {{FICHIERS_OU_LIENS}}

[SKILLS]
1. `brainstorming` → exploration du besoin (pas de code)
2. `ui-ux-pro-max` → si UI : 2-3 directions visuelles après le cadrage fonctionnel

[EXCLUSIONS]
Pas de code ni de choix de stack. Ne pas inventer de contraintes non données.

[ITÉRATION] Poser ≤ 3 questions regroupées avant le brief final.
```

**Template `/docs/brief.md`** :
```md
# Brief — {{NOM_PROJET}} · {{DATE}}
- Problème / cible / promesse :
- MVP (périmètre minimum) :
- Parcours principal (étape par étape) :
- Critères d'acceptation vérifiables :
- Hypothèses et risques :
- Hors périmètre (explicite) :
- Décisions à valider :
```

**Critère de sortie** : un utilisateur peut décrire le parcours principal ; les critères d'acceptation ne sont pas ambigus.

---

### Jalon B — Plan d'Exécution

**But** : décomposer le MVP en lots ordonnés sans générer de code.
**Skills** : `planification` · `doc-coauthoring` · `slides` (si présentation stakeholders)

```
[PERSONA] Chef de projet technique, livraisons itératives.

[OBJECTIF] À partir de /docs/brief.md, produire un plan en lots (3–7),
chacun démontrable et testable, pour éviter un développement monolithique.

[SITUATION] Consulter /docs/decisions.md si existant.
Consulter le Router (section 4) pour {{TYPE_PROJET}}.

[SKILLS]
`planification` → format TDD : chaque lot = critère de "terminé" explicite

[EXCLUSIONS] Pas de code. Pas de granularité excessive. Réutiliser la stack existante.

[ITÉRATION] Proposer le plan, demander validation avant construction.
```

**Template `/docs/plan.md`** :
```md
# Plan d'exécution — {{NOM_PROJET}} · {{DATE}}
## Décisions verrouillées
## Lot 1 — fondations
- [ ] action · fichiers touchés · validation · skill mobilisé
## Lot 2 — flux principal
- [ ] action · fichiers touchés · validation · skill mobilisé
## Lot 3 — qualité et livraison
- [ ] action · fichiers touchés · validation · skill mobilisé
## Dépendances, risques et rollback
```

**Critère de sortie** : le plan indique l'ordre, les dépendances et la commande ou le scénario de validation de chaque lot.

---

### Jalon C — Architecture Juste Suffisante

**But** : figer les choix techniques structurants — uniquement si la complexité le justifie (cf. Router).
**Skills** : `doc-coauthoring` · `managing-python-dependencies` (si back Python) · `gcloud-auth-verification` (si GCP) · skill DB selon le choix

> ⚡ Pour une landing page ou un site simple : documenter seulement 3 lignes dans le plan — pas de fichier séparé.

```
[PERSONA] Architecte logiciel senior, orienté simplicité, anti sur-ingénierie.

[OBJECTIF] ADR léger pour {{TYPE_PROJET}} : figer stack, flux, intégrations.
Base : /docs/brief.md + /docs/plan.md

[SKILLS SELON CONTEXTE]
- Backend Python → `managing-python-dependencies`
- GCP → `gcloud-auth-verification` + skill GCP correspondant
- Base de données → `cloud-sql-postgres-admin` | `firestore-data` | `alloydb-*`

[EXCLUSIONS]
Pas de composants non justifiés par le brief. Justifier chaque choix en une phrase.
Ne jamais ajouter de microservices pour une landing page.

[ITÉRATION] Si plusieurs stacks plausibles → tableau comparatif → attendre arbitrage.
```

**Template `/docs/architecture.md`** :
```md
# Architecture — {{NOM_PROJET}} · {{DATE}}
## Contexte et contraintes
## Vue d'ensemble
[Client] → [API / automatisation] → [Données / services externes]
## Composants et responsabilités
## Modèle de données et flux
## Contrats (routes, événements, entrées/sorties)
## Auth, autorisation et secrets
## Fiabilité (erreurs, idempotence, limites, observabilité)
## Performance et accessibilité
## Déploiement, sauvegarde et rollback
## ADR — décisions et compromis
```

**Exigences spécifiques par domaine** :
- **Automatisation** : déclencheur, état, retries/backoff, idempotence, limites de débit, journalisation, alertes, procédure de reprise.
- **SaaS/Fullstack** : frontières client/API, rôles, multi-tenant si requis, migrations, validation serveur, quotas et audit.
- **Dashboard** : provenance, fraîcheur, granularité, filtres, agrégations, état vide/erreur, export.
- **Jeu navigateur** : boucle de jeu, états, contrôles, sauvegarde, performances mobile, écran de fin.
- **Storefront** : catalogue, panier, stocks, taxes/livraison, paiement par prestataire, confirmation, conformité. **Ne jamais implémenter le traitement de carte soi-même.**

**Critère de sortie** : chaque composant a une responsabilité, chaque donnée critique a un propriétaire, les défaillances prévisibles ont une réponse.

---

### Jalon D — Design & Expérience Utilisateur

**But** : concevoir avant d'implémenter, au niveau adapté au produit.

| Besoin | Skill à activer |
|--------|----------------|
| Maquettes UI écrans complets | `stitch` |
| Palette · typo · patterns UX | `ui-ux-pro-max` |
| Design system (tokens CSS) | `design-system` |
| Direction visuelle frontend | `frontend-design` |
| Identité de marque + copy | `brand` |
| Thème rapide cohérent | `theme-factory` |
| Visuels statiques (hero, OG, favicon) | `canvas-design` |
| Bannières réseaux sociaux | `banner-design` |
| Composants shadcn/Tailwind | `ui-styling` |
| Art génératif / jeu | `algorithmic-art` |

```
[PERSONA] Designer produit senior, esthétique moderne, cohérence design system.

[OBJECTIF] Direction visuelle pour {{TYPE_PROJET}} avant tout code frontend.

[SITUATION]
- Ton : {{TON_VISUEL}} | Référence : {{IMAGE_OU_LIEN}}
- Réutiliser le design system existant si présent. À défaut, fixer 1 palette,
  1 échelle typographique, espacements, rayons et règles de contraste.

[SKILLS — dans cet ordre]
1. `stitch` → maquettes écrans clés (desktop + mobile) via StitchMCP
2. `ui-ux-pro-max` → validation UX, patterns, palettes
3. `design-system` → tokens CSS (variables, espacement, typo)
4. `frontend-design` → direction visuelle intentionnelle
5. `brand` → si identité de marque complète requise
6. `canvas-design` → hero image, Open Graph, favicon
7. `banner-design` → bannières LinkedIn, Twitter/X si marketing

[EXCLUSIONS] Pas de "template Bootstrap-like" générique. Chaque choix est intentionnel.
N'utiliser un skill image/Figma que si cela sert réellement un livrable demandé.
Si design-to-code : analyser l'image en zones/composants/responsive/a11y —
ne pas prétendre extraire des éléments non visibles.

[ITÉRATION] 2 directions distinctes → choisir avant maquettes définitives.
```

**Template `/docs/design-spec.md`** :
```md
# Design Spec — {{NOM_PROJET}} · {{DATE}}
## Direction visuelle retenue (palette, typo, espacements, border-radius)
## Inventaire d'écrans et composants
## Parcours et microcopies
## Responsive (breakpoints)
## Accessibilité (clavier, focus, contraste, labels ARIA)
## États particuliers (chargement, vide, erreur, non autorisé, mobile)
```

**Critères spécifiques** :
- **Landing** : proposition de valeur visible sans scroll, CTA primaire, preuve de confiance, contenu scannable, responsive, perf.
- **Dashboard** : une question métier par graphique, choix de graphique justifié, libellés/infobulles, filtre, légende, données manquantes.
- **Storefront** : recherche/catégories, fiche produit, panier, checkout clair, signaux de confiance, mobile.

**Critère de sortie** : l'interface et ses états critiques peuvent être construits sans nouvelles décisions de design importantes.

---

### Jalon E — Construction Incrémentale

**But** : coder, tester, livrer — en suivant strictement le plan et l'architecture validés.

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
| Opération destructive | `accidental-data-loss-prevention` ← **OBLIGATOIRE** |

```
[PERSONA] Développeur senior full-stack, livraisons par petites itérations testables.

[OBJECTIF] Implémenter le lot {{NUMERO_LOT}} du plan (/docs/plan.md),
en respectant l'architecture et le design validés.

[SITUATION] Type : {{TYPE_PROJET}}

[SKILLS]
1. Identifier les skills du Router (section 4) pour {{TYPE_PROJET}}
2. Vérifier l'existence dans `~/.gemini/config/skills/`
3. Si skill manquant → signaler AVANT de commencer

[SÉQUENCE PAR TÂCHE]
a) Relire le lot concerné et les conventions du repo
b) Écrire le test qui échoue (TDD)
c) Implémenter le chemin le plus court, interfaces simples
d) Lancer formatage, lint, tests ciblés → corriger les erreurs introduites
e) Commit
f) Mettre à jour /docs/changelog.md uniquement si la réalité diffère de la décision

[EXCLUSIONS]
- Ne pas toucher aux fichiers hors périmètre du lot
- Ne pas réécrire l'architecture ou le design déjà validés
- Si blocage impose une modification → signaler, proposer, attendre validation

[AVANT TOUTE ACTION DESTRUCTIVE]
Activer `accidental-data-loss-prevention` → résumer 5 lignes → attendre feu vert explicite.
```

**Qualité non négociable** (vérifier à chaque lot) :
- Entrées validées côté serveur ; messages d'erreur utiles mais non sensibles
- États de chargement, vide et erreur visibles dans l'UI
- HTML sémantique, navigation clavier, focus perceptible, contraste suffisant
- Pas de données simulées présentées comme réelles — étiqueter les mocks et fixtures
- Pas de secrets, clés privées, ni fichiers locaux sensibles dans Git
- Pas de `TODO` bloquant déguisé en fonctionnalité terminée

**Résumé de lot obligatoire** (5 lignes avant de passer au lot suivant) :
```
- Réalisé :
- Comment tester :
- Ce qui reste :
- Risques identifiés :
- Décision attendue (si applicable) :
```

---

### Jalon F — Vérification, Audit & Livraison

**But** : valider la qualité, corriger, déployer.
**Skills** : `webapp-testing` · `a11y-debugging` · `debug-optimize-lcp` · `memory-leak-debugging` · `chrome-devtools` · `troubleshooting`

```
[PERSONA] Ingénieur QA senior et expert performance web.

[OBJECTIF] Valider {{NOM_PROJET}} avant mise en production.

[SKILLS — séquence à respecter]
1. `webapp-testing` → tests fonctionnels (scénarios, mobile 375px + desktop 1440px)
2. `a11y-debugging` → audit WCAG AA (HTML, ARIA, contraste, clavier, tap 44px)
3. `debug-optimize-lcp` → Core Web Vitals (LCP < 2.5s, CLS < 0.1, INP < 200ms)
4. `memory-leak-debugging` → si session longue ou état complexe
5. `chrome-devtools` → inspection réseau, console, profiling si problème persistant

[SÉQUENCE]
a) Formatage / lint
b) Vérification de types / build
c) Tests unitaires ciblés puis complets si coût raisonnable
d) Test du parcours principal (E2E ou procédure manuelle)
e) Audit rapide : responsive, a11y, erreurs réseau, variables d'env
f) Revue du diff Git (fichiers accidentels, changements hors périmètre)

Pour une automatisation : déclencher un essai contrôlé, prouver le résultat,
tester au moins un échec/retry si applicable.

[AVANT DÉPLOIEMENT]
Présenter : build command · variables d'env requises · migrations · stratégie de rollback.
Attendre autorisation explicite avant d'exécuter.
```

**Rapport de livraison obligatoire** (`/docs/audit.md`) :
```md
# Livraison — {{NOM_PROJET}} · {{DATE}}
- Réalisé :
- Parcours vérifié :
- Fichiers / composants majeurs :
- Validations exécutées et résultat :
- Configuration requise (sans valeurs de secrets) :
- Limites / risques restants :
- Prochaine action suggérée :
```

---

## 6. Invocations Compactes (à coller dans une nouvelle session)

### A. Démarrer ou reprendre un projet

```
Suis AGENT-PROTOCOL.md strictement. Objectif : [OBJECTIF]. Type : [TYPE].
Commence par lire README*, AGENTS.md et git log --oneline -5.
Identifie les skills globaux pertinents dans ~/.gemini/config/skills/ sans scan massif.
Affiche le registre de capacités retenues et un résumé opérationnel ≤ 250 mots.
Exécute uniquement le Jalon [A/B/C/D/E/F].
Arrête-toi au critère de sortie et pose ≤ 3 questions seulement si une décision bloquante demeure.
```

### B. Construire un MVP de bout en bout

```
Suis AGENT-PROTOCOL.md. Construis le MVP suivant :
[OBJECTIF] (type : [TYPE], cible : [CIBLE], contraintes : [CONTRAINTES])

Découvre une fois les skills globaux pertinents, utilise seulement ceux qui apportent une valeur nette.
Exécute les Jalons A → F avec gates :
- Soumettre brief + plan + architecture/design pour validation avant construction
  si une décision est irréversible ; sinon avancer avec hypothèses réversibles déclarées.
- Implémenter par lots, tester chaque lot, terminer par le rapport de livraison.

Pas d'installation, appel externe payant ni déploiement sans accord explicite.
```

### C. Ajouter une fonctionnalité dans un dépôt existant

```
Suis AGENT-PROTOCOL.md en mode changement ciblé.
Fonctionnalité : [FONCTIONNALITÉ]

Lis les instructions et le code strictement nécessaires.
Détecte les skills pertinents une seule fois.
Donne un mini-plan (≤ 7 étapes) avec validations.
Après accord implicite si le changement est réversible :
implémente en petits lots, lance les validations pertinentes, fournis le rapport final avec les limites.
```

### D. Corriger un bug efficacement

```
Suis AGENT-PROTOCOL.md en mode diagnostic frugal.
Symptôme : [SYMPTÔME]

Reproduis d'abord le problème.
Isole la cause avec le moins de fichiers/outils possible.
Propose la correction minimale et un test anti-régression.
Utilise les skills globaux seulement s'ils réduisent réellement l'incertitude.
Ne refactorise pas hors périmètre.
Conclusion : cause racine · correction · validations · risque résiduel.
```

### E. Entrée unique — Projet complet (prompt principal)

```
Suis le fichier AGENT-PROTOCOL.md présent à la racine du projet.
Skills disponibles : ~/.gemini/config/skills/ (93 compétences).

1. Détermine {{TYPE_PROJET}} et remplis la fiche YAML (section 1).
2. Consulte le Router (section 4) pour les skills à mobiliser par jalon.
3. Exécute les jalons dans l'ordre :
   A : Brief          → /docs/brief.md
   B : Plan           → /docs/plan.md
   C : Architecture   → /docs/architecture.md (si complexité le justifie)
   D : Design         → /docs/design-spec.md + maquettes Stitch
   E : Construction   → code + /docs/changelog.md (par lot)
   F : Tests/Deploy   → /docs/audit.md
4. Avant chaque jalon : pose ≤ 3 questions si informations manquantes,
   attends validation avant de passer au jalon suivant.
5. Ne relis pas un skill déjà chargé dans la session.
6. Si un skill du Router n'existe pas dans ~/.gemini/config/skills/, signale-le.

Description : {{DESCRIPTION_IDEE}}
Type pressenti : {{TYPE_PROJET}}
```

---

## 7. Règle de Décision Finale

En cas de conflit entre objectifs :

**Sécurité & exactitude > Instructions locales du dépôt > Maintenabilité > Vitesse > Embellissement**

> Toute affirmation de succès doit être appuyée par une commande, un test ou un scénario effectivement exécuté.

---

## 8. Checklist Finale (contrôle qualité & tokens)

- [ ] README + AGENTS.md + git state lus avant toute action
- [ ] Découverte des skills effectuée une seule fois — registre de session rempli
- [ ] Fiche YAML (section 1) complétée ou fiche d'hypothèses produite
- [ ] Chaque jalon a produit un fichier `/docs/` court et daté
- [ ] L'architecture est proportionnée à la taille réelle du projet
- [ ] Le design (`stitch` + `design-system`) validé **avant** le début du code
- [ ] Chaque lot de construction a été testé avant le suivant
- [ ] Qualité non négociable vérifiée à chaque lot (validation serveur, états UI, a11y, pas de secrets)
- [ ] `/docs/decisions.md` reflète tous les choix figés
- [ ] `accidental-data-loss-prevention` activé avant toute opération destructive
- [ ] Core Web Vitals vérifiés (`debug-optimize-lcp`)
- [ ] Accessibilité WCAG AA auditée (`a11y-debugging`)
- [ ] Rapport de livraison `/docs/audit.md` produit
- [ ] Aucun secret dans Git — `.env.example` documenté

---

## 9. Index Rapide — Skills par Jalon

| Jalon | Skills essentiels | Skills optionnels |
|-------|------------------|------------------|
| **A · Brainstorming** | `brainstorming` | `ui-ux-pro-max` `planification` |
| **B · Plan** | `planification` | `doc-coauthoring` `slides` |
| **C · Architecture** | `doc-coauthoring` | `managing-python-dependencies` `gcloud-auth-verification` `cloud-sql-postgres-admin` `firestore-data` |
| **D · Design** | `stitch` `design-system` `frontend-design` | `ui-ux-pro-max` `brand` `canvas-design` `banner-design` `theme-factory` `ui-styling` `algorithmic-art` |
| **E · Construction** | `modern-web-guidance` + skills Router | `web-artifacts-builder` `claude-api` `mcp-builder` `google-antigravity-sdk` `managing-python-dependencies` `building-data-apps` `remotion-best-practices` `accidental-data-loss-prevention` |
| **F · Tests/Deploy** | `webapp-testing` `a11y-debugging` `debug-optimize-lcp` | `memory-leak-debugging` `chrome-devtools` `troubleshooting` |

---

*Protocole POSER v3.0 · 2026-07-20 · Compatible Antigravity (Gemini) & Claude Code*
*Skills disponibles : 93 · Dossier : `~/.gemini/config/skills/`*
*Dupliquer par projet · remplir les `{{VARIABLES}}` · placer à la racine aux côtés de `CLAUDE.md`*
