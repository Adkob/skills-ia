# Agent Protocol — Construction de Projets Numériques
> Version 1.0 · Compatible Antigravity (Gemini) & Claude Code
> Mobilise les skills disponibles dans `~/.gemini/config/skills/`
> Placer dans `directives/agent-protocol.md` ou copier tel quel dans un prompt

---

## Comment utiliser ce document

Ce fichier contient des **prompts prêts à l'emploi** organisés par :
1. **Phase** (6 étapes du cycle de vie projet)
2. **Type de projet** (8 catégories)

**Règle d'or** : Copie-colle le prompt de la phase, adapte les `[VARIABLES]`, envoie.
L'agent activera automatiquement les skills appropriés.

**Économie de tokens** : Chaque prompt = une seule session par phase.
L'agent travaille, tu valides, tu passes à la phase suivante.

---

## PHASE 0 — Initialisation du Projet

> Envoyer en **premier message** de chaque nouveau projet.

```
Je démarre un nouveau projet : [NOM DU PROJET]
Type : [landing page / dashboard / SaaS / jeu / fullstack app / boutique / automatisation / site web]
Contexte : [2-3 phrases décrivant le problème ou l'opportunité]
Cible : [utilisateurs finaux]
Stack technique souhaitée (si connue) : [ou "au choix"]
Contraintes : [délai, budget, intégrations obligatoires, ou "aucune"]

Utilise le protocole d'architecture à 3 couches (directives → orchestration → exécution).
Commence par activer la compétence `brainstorming` pour explorer les besoins avant toute implémentation.
```

---

## PHASE 1 — Brainstorming & Exploration

> **Skills** : `brainstorming`, `ui-ux-pro-max`, `stitch`
> **Objectif** : Comprendre, explorer, aligner — AUCUN code à cette étape.

### 1A · Brainstorming Général

```
[SKILL: brainstorming]

Projet : [NOM]
Type : [TYPE]

Explore avec moi les besoins réels de ce projet.
Pose-moi des questions une par une pour comprendre :
1. Le problème core à résoudre
2. Les utilisateurs (personas, douleurs, attentes)
3. Les fonctionnalités essentielles vs nice-to-have
4. Les contraintes techniques et business
5. Les métriques de succès (comment saurons-nous que c'est réussi ?)

Ne commence pas à coder ou planifier. Explore d'abord.
```

### 1B · Exploration UI/UX

```
[SKILL: ui-ux-pro-max]

Contexte : [RÉSUMÉ DU PROJET EN 2 PHRASES]

Recommande-moi :
- 3 styles visuels possibles (palette, typographie, mood board verbal)
- Les patterns UX clés pour ce type de produit
- Les 5 écrans / vues essentiels à concevoir en priorité
- Les risques UX à anticiper

Format : tableaux comparatifs + liste priorisée.
```

### 1C · Génération Maquettes Stitch

```
[SKILL: stitch]

Crée un projet Stitch pour : [NOM DU PROJET]
Design system : couleur principale [HEX], style [moderne/minimaliste/bold/glassmorphism], mode [LIGHT/DARK]
Police : [Inter / Manrope / Space Grotesk / au choix]
Device : [DESKTOP / MOBILE / les deux]

Génère les écrans suivants :
1. [Nom écran 1] — [description en 1 phrase]
2. [Nom écran 2] — [description en 1 phrase]
3. [Nom écran 3] — [description en 1 phrase]

Pour chaque écran : style cohérent, sections [liste des sections clés].
Génère 3 variantes de l'écran principal (creativeRange: EXPLORE).
```

---

## PHASE 2 — Planification & Architecture

> **Skills** : `planification`, `doc-coauthoring`, `slides`, `docx`
> **Objectif** : Plan d'implémentation + document d'architecture.

### 2A · Plan d'Implémentation

```
[SKILL: planification]

Projet : [NOM]
Objectif : [UNE PHRASE]

Architecture envisagée :
- Frontend : [React/Next.js/Vite/HTML vanilla/autre]
- Backend : [Node.js/Python/Firebase/Supabase/serverless/aucun]
- Base de données : [PostgreSQL/SQLite/Firestore/aucune]
- Déploiement : [Vercel/Netlify/GCP/local]

Fonctionnalités à implémenter :
1. [Feature 1]
2. [Feature 2]
3. [Feature 3]

Génère un plan d'implémentation complet avec :
- Structure des fichiers
- Tâches bite-sized avec tests TDD
- Ordre de développement (dépendances d'abord)
- Commandes exactes à chaque étape

Sauvegarde dans docs/plan/[NOM]-[DATE].md
```

### 2B · Document d'Architecture

```
[SKILL: doc-coauthoring]

Rédige le document d'architecture technique pour : [NOM DU PROJET]

Sections requises :
1. Vue d'ensemble et objectifs
2. Diagramme d'architecture (Mermaid)
3. Stack technique justifiée
4. Structure des répertoires
5. Modèle de données (entités principales)
6. API et flux de données
7. Stratégie de sécurité
8. Plan de déploiement
9. Risques techniques et mitigations

Contexte : [RÉSUMÉ TECHNIQUE EN 3 PHRASES]
Stack : [STACK CHOISIE]

Format : Markdown, à committer dans docs/architecture.md
```

### 2C · Présentation du Plan (stakeholders)

```
[SKILL: slides]

Crée une présentation de 8 slides pour valider le plan du projet [NOM].

Slides :
1. Titre + tagline
2. Problème résolu
3. Solution proposée + capture maquette
4. Architecture technique (schéma simplifié)
5. Roadmap / phases de développement
6. Stack technique + justification
7. Métriques de succès
8. Prochaines étapes

Style : moderne, professionnel, dark mode, accent [COULEUR].
```

---

## PHASE 3 — Design & Identité Visuelle

> **Skills** : `design`, `design-system`, `frontend-design`, `brand`, `theme-factory`, `canvas-design`, `banner-design`, `stitch`
> **Objectif** : Produire tous les assets visuels avant de coder.

### 3A · Design System Complet

```
[SKILL: design-system]

Crée le design system complet pour [NOM DU PROJET].

Identité : [description du produit en 1 phrase]
Valeurs : [ex: moderne, fiable, accessible, fun]
Cible : [description des utilisateurs]

Génère :
1. Palette de couleurs (primary, secondary, accent, neutral, semantic)
2. Typographie (titres, corps, code, labels) avec tailles et poids
3. Système d'espacement (base 4px)
4. Tokens de bordure, ombre, border-radius
5. Variables CSS/Tailwind correspondantes
6. Exemples : bouton, carte, formulaire, badge

Format : fichier CSS variables + documentation Markdown.
```

### 3B · Identité de Marque

```
[SKILL: brand]

Développe l'identité de marque pour [NOM DU PROJET].

Description : [ce que fait le produit]
Ton : [professionnel / décontracté / technique / ludique / premium]
Secteur : [SaaS / e-commerce / créatif / data / outil dev]

Produis :
1. Brand voice guide (ton, langage, ce qu'on dit / ne dit pas)
2. Tagline principale + 3 alternatives
3. Messages clés par persona
4. Palette émotionnelle et visuels suggérés
5. Copy pour : hero section, CTA, email d'onboarding
```

### 3C · Thème Visuel Rapide

```
[SKILL: theme-factory]

Applique un thème visuel cohérent pour [NOM DU PROJET].

Style : [moderne sombre / minimaliste blanc / coloré vibrant / glassmorphism / néon tech / corporate bleu]
Secteur : [TYPE DE PROJET]

Génère le thème complet : couleurs, typographie, composants styled.
```

### 3D · Assets Visuels

```
[SKILL: canvas-design]

Crée les visuels pour [NOM DU PROJET] :
1. Hero image (1920x1080) — [description du sujet]
2. Image Open Graph (1200x630) — [description]
3. Favicon et icône app (512x512) — [style, icône]
Style : [STYLE DU PROJET], palette [COULEURS PRINCIPALES].

[SKILL: banner-design]
Bannières réseaux sociaux :
- LinkedIn (1200x627) — [message clé]
- Twitter/X (1500x500) — [message]
```

---

## PHASE 4 — Développement & Construction

> **Skills** : `modern-web-guidance`, `frontend-design`, `web-artifacts-builder`, `mcp-builder`, `managing-python-dependencies`, `chrome-extensions`, `claude-api`
> **Objectif** : Construire le produit, fichier par fichier, en TDD.

### 4A · Démarrage Projet Web

```
[SKILL: modern-web-guidance]
[SKILL: frontend-design]

Initialise le projet [NOM] avec :
- Framework : [Next.js 14 App Router / Vite + React / HTML+CSS+JS vanilla]
- Styling : [CSS Modules / Tailwind v3 / Vanilla CSS]
- Auth : [NextAuth / Supabase Auth / aucune]
- DB : [Prisma + PostgreSQL / Supabase / Firebase / aucune]

Structure de fichiers :
[COLLER ICI LA STRUCTURE DU PLAN D'ARCHITECTURE]

Commence par :
1. Initialiser le projet (commandes exactes)
2. Configurer le design system (variables CSS ou Tailwind config)
3. Créer les composants de base (Layout, Header, Footer, Button, Card)
4. Implémenter la page d'accueil

Respecte : sémantique HTML5, accessibilité ARIA, responsive mobile-first.
```

### 4B · Feature par Feature

```
Implémente la feature : [NOM DE LA FEATURE]

Contexte du projet : [NOM] — [STACK]
Fichiers concernés :
- Créer : [liste des nouveaux fichiers]
- Modifier : [liste des fichiers existants]

Comportement attendu :
[DESCRIPTION PRÉCISE]

Contraintes :
- Tests unitaires requis avant l'implémentation (TDD)
- Commandes de test : [ex: npm test]
- Commit après chaque sous-tâche validée

Commence par écrire le test qui échoue, puis implémente.
```

### 4C · API & Backend

```
Implémente les endpoints API pour [NOM DU PROJET] :

[SKILL: managing-python-dependencies] (si backend Python)

Endpoint 1 : [METHOD] [/path]
- Input : [schema]
- Output : [schema]
- Logique : [description]
- Erreurs : [liste]

Endpoint 2 : [METHOD] [/path]
[...]

Génère aussi :
- Schéma de validation (Zod / Pydantic / Joi)
- Tests d'intégration
- Documentation OpenAPI inline

[SKILL: accidental-data-loss-prevention]
Avant tout DELETE ou opération destructive, demander confirmation.
```

### 4D · Intégration IA (Claude/Gemini)

```
[SKILL: claude-api]

Intègre l'IA dans [NOM DU PROJET] pour : [DESCRIPTION DE LA FONCTIONNALITÉ]

Modèle : [claude-sonnet-4-5 / gemini-2.0-flash / au choix]
Type d'appel : [streaming / one-shot / multi-turn]
Rôle système : [description du rôle de l'IA]

Implémente :
1. Client API avec gestion des erreurs et retry
2. Gestion du streaming si applicable
3. Prompt engineering optimisé
4. Composant UI d'affichage de la réponse
5. Tests avec mocks de l'API
```

### 4E · Scripts d'Automatisation

```
[SKILL: managing-python-dependencies]

Crée le script : execution/[nom-script].py
Tâche : [DESCRIPTION DE CE QUE LE SCRIPT DOIT FAIRE]

Ce script doit :
1. [Action 1]
2. [Action 2]
3. [Action 3]

Inputs : [paramètres / variables d'env depuis .env]
Outputs : [format de sortie, fichiers produits]

Structure :
- Commentaires en-tête (purpose, usage, dependencies)
- Argparse pour les paramètres CLI
- Logging DEBUG/INFO/ERROR
- Mode --dry-run

Génère aussi directives/[nom-script].md (quoi/comment/cas limites).
Exécute et montre la sortie.
```

---

## PHASE 5 — Tests, Audit & Déploiement

> **Skills** : `webapp-testing`, `a11y-debugging`, `debug-optimize-lcp`, `memory-leak-debugging`, `chrome-devtools`
> **Objectif** : Valider la qualité avant mise en production.

### 5A · Tests Fonctionnels

```
[SKILL: webapp-testing]

Teste [NOM] sur [URL ou localhost:PORT].

Scénarios à valider :
1. [Scénario 1 — ex: inscription utilisateur]
   - Actions : [séquence]
   - Résultat attendu : [comportement]
2. [Scénario 2]
3. [Scénario 3]

Pour chaque scénario :
- Screenshot avant/après actions clés
- Vérifier messages d'erreur et états de chargement
- Tester mobile (375px) et desktop (1440px)
- Reporter bugs : description, étapes, screenshot
```

### 5B · Audit Accessibilité

```
[SKILL: a11y-debugging]

Audite l'accessibilité de [URL].

Vérifie :
1. Structure sémantique HTML (headings, landmarks)
2. Labels ARIA sur éléments interactifs
3. Navigation clavier (Tab, Enter, Escape)
4. Contrastes de couleur (WCAG AA minimum)
5. Zones de tap mobile (44px minimum)
6. Messages d'erreur de formulaires accessibles

Produis : rapport avec score, issues par sévérité, corrections recommandées.
```

### 5C · Optimisation Performance

```
[SKILL: debug-optimize-lcp]

Analyse et optimise les performances de [URL].

Cibles : LCP < 2.5s · CLS < 0.1 · INP < 200ms

Vérifie :
1. Ressources bloquantes (CSS/JS critique)
2. Images (format, taille, lazy loading, priority)
3. Fonts (FOUT, preload)
4. Render-blocking scripts
5. Cache et CDN

Produis : métriques actuelles, causes, actions correctives priorisées.
```

### 5D · Déploiement

```
Déploie [NOM] sur [Vercel / Netlify / GCP / VPS].

Prérequis :
- Build command : [npm run build ou autre]
- Output directory : [dist / .next / build]
- Variables d'env : [liste des clés sans valeurs]
- Domain : [domaine ou "auto-généré"]

Génère :
1. Commande de déploiement complète
2. Config provider (vercel.json / netlify.toml / dockerfile)
3. Fichier .env.example documenté
4. Checklist de validation post-déploiement
```

---

## PROMPTS PAR TYPE DE PROJET

### 🚀 SaaS Application

```
[SKILL: brainstorming] + [SKILL: planification] + [SKILL: stitch] + [SKILL: design-system]

Je construis un SaaS : [NOM]
Problème résolu : [DESCRIPTION]
Modèle de revenus : [freemium / subscription / usage-based]
Utilisateurs cibles : [PERSONAS]

Phase 1 — Explorer les fonctionnalités core et le MVP minimum viable.
Lister les features : Must Have / Should Have / Could Have.

Phase 2 — Stack recommandée pour SaaS scalable (auth, billing Stripe, multi-tenancy).
Générer la structure complète des fichiers.

Phase 3 — Via Stitch : dashboard utilisateur, pricing, onboarding (3 steps), settings.
Design system : couleur [HEX], style [STYLE].
```

### 🛍️ Boutique en Ligne (Storefront)

```
[SKILL: brainstorming] + [SKILL: stitch] + [SKILL: design] + [SKILL: brand]

Je construis une boutique en ligne pour : [PRODUIT/NICHE]
Budget client moyen : [FOURCHETTE]
Nombre de produits : [ESTIMATION]

Via Stitch — générer :
- Page d'accueil hero + featured products
- Catalogue avec filtres
- Page produit avec galerie
- Panier + checkout (3 étapes)
- Compte utilisateur

Intégrations : [Stripe / Shopify / WooCommerce / custom]
Design : [premium/accessible/coloré/minimaliste], accent [COULEUR]
Inclure : SEO, schema.org produits, Core Web Vitals.
```

### 📊 Dashboard & Data App

```
[SKILL: building-data-apps] + [SKILL: stitch] + [SKILL: ui-ux-pro-max]

Je construis un dashboard pour : [OBJECTIF]
Source de données : [API / CSV / PostgreSQL / BigQuery / Firestore]
Utilisateurs : [PROFIL]

Via Stitch — générer :
- Overview avec 4 KPIs
- Graphiques : [ligne / bar / pie / scatter]
- Table de données avec tri/filtre/export
- Filtres temporels (7j / 30j / custom)

Stack : React + Recharts/Nivo ou Streamlit (Python)
Données : [SCHÉMA OU DESCRIPTION]

Générer d'abord avec données mock, puis connecter à [SOURCE].
```

### 🎮 Jeu Navigateur

```
[SKILL: brainstorming] + [SKILL: modern-web-guidance] + [SKILL: algorithmic-art]

Je construis un jeu navigateur : [NOM — CONCEPT EN 1 PHRASE]
Genre : [puzzle / platformer / arcade / stratégie / RPG text]
Technologie : [Canvas API / Three.js / Phaser / HTML+CSS pur]

Mécaniques :
1. [Mécanique principale]
2. [Règles de victoire/défaite]
3. [Progression]

Générer :
- Boucle de jeu principale (game loop)
- Moteur de rendu (selon techno)
- Système de score + highscore (localStorage)
- Écran titre + game over
- Contrôles clavier + touch mobile

Commencer par la version la plus simple jouable, itérer ensuite.
```

### 🌐 Landing Page

```
[SKILL: stitch] + [SKILL: frontend-design] + [SKILL: brand] + [SKILL: modern-web-guidance]

Landing page pour : [PRODUIT/SERVICE]
Objectif de conversion : [email signup / achat / demo request / téléchargement]
Audience : [DESCRIPTION]

Sections :
1. Hero — [accroche + CTA]
2. Problème/Solution — [pain points + bénéfices]
3. Fonctionnalités — [3-5 features avec icônes]
4. Social proof — [testimonials / logos / stats]
5. Pricing — [plans si applicable]
6. FAQ — [objections courantes]
7. CTA final

Via Stitch : maquette desktop + mobile d'abord.
Via brand : copy pour chaque section.
Optimisation : SEO meta tags, Core Web Vitals, schema.org, Open Graph.
```

### 📱 Application Fullstack

```
[SKILL: planification] + [SKILL: modern-web-guidance] + [SKILL: managing-python-dependencies]

Application fullstack : [NOM]
Fonctionnalité principale : [DESCRIPTION EN 1 PHRASE]

Frontend : [Next.js 14 / React + Vite / Vue / autre]
Backend : [Node.js Express / FastAPI / Next.js API Routes]
Base de données : [PostgreSQL / MongoDB / SQLite / Supabase]
Auth : [NextAuth / Supabase Auth / Auth0 / JWT custom]
Hébergement : [Vercel + Railway / Fly.io / GCP / autre]

Ordre de génération :
1. Schéma de base de données + migrations
2. API RESTful avec validation et tests
3. Frontend avec gestion d'état (Zustand / Redux / Context)
4. Authentification complète
5. Déploiement et variables d'environnement

Chaque étape : tests avant implémentation, commit après validation.
```

### 🤖 Automatisation de Service/Tâche/Processus

```
[SKILL: planification] + [SKILL: managing-python-dependencies]

Je veux automatiser : [DESCRIPTION DE LA TÂCHE]
Déclencheur : [manuel / cron / webhook / événement]
Source de données : [API / fichier / base de données / scraping]
Sortie : [email / fichier / base de données / Google Sheets / Slack]

Générer execution/[nom-tache].py :
- Connexion à la source (credentials depuis .env)
- Logique de traitement
- Gestion des erreurs avec retry
- Logging structuré
- Mode --dry-run
- Notification de succès/échec

Générer directives/[nom-tache].md (quoi/comment/cas limites).
Tester immédiatement et montrer la sortie.
```

### 🎨 Design depuis Image (Design mon Code)

```
[SKILL: stitch] + [SKILL: frontend-design] + [SKILL: modern-web-guidance]

J'ai une image de design que je veux transformer en code.
[JOINDRE L'IMAGE]

Analyser et identifier :
1. Structure de layout (grid, flexbox, sections)
2. Palette de couleurs exacte (HEX)
3. Typographie (tailles, poids, familles)
4. Composants réutilisables
5. Interactions probables

Générer :
- Variables CSS du design system extrait
- Composants React/HTML+CSS pixel-perfect
- Layout responsive (breakpoint mobile 768px)
- Animations/transitions si visibles

Commencer par le composant le plus complexe.
```

---

## CHECKLIST ANTI-GASPILLAGE DE TOKENS

Avant d'envoyer un prompt, vérifier :

- [ ] **Contexte minimal** : uniquement ce qui est nécessaire (pas de code entier sauf si demandé)
- [ ] **Une phase à la fois** : brainstorming ET code dans le même message = gaspillage
- [ ] **Skill déclaré** : mentionner `[SKILL: nom]` pour orienter l'agent
- [ ] **Variables remplies** : tous les `[CROCHETS]` sont remplacés par de vraies valeurs
- [ ] **Format de sortie précis** : spécifier Markdown / fichier / code / tableau
- [ ] **Objectif unique** : chaque prompt = un livrable mesurable

---

## ORDRE RECOMMANDÉ PAR PHASE

```
Phase 0 : Initialisation        → Prompt 0
Phase 1 : Brainstorming         → 1A + 1B (+ 1C si maquettes rapides)
Phase 2 : Planification         → 2A + 2B (+ 2C si présentation stakeholders)
Phase 3 : Design                → 3A + 3B + 3D (+ 3C optionnel)
Phase 4 : Développement         → 4A → 4B (répété par feature) → 4C si API → 4D si IA
Phase 5 : Tests & Déploiement   → 5A + 5B + 5C + 5D
```

**Durée estimée par phase** (projet moyen) :
| Phase | Durée | Livrable |
|-------|-------|---------|
| 0-1 Exploration | 15-30 min | Brief validé + maquettes |
| 2 Planification | 30-60 min | Plan + architecture |
| 3 Design | 30-45 min | Design system + assets |
| 4 Développement | variable | Code fonctionnel par feature |
| 5 Tests/Déploiement | 30-60 min | App validée + en ligne |

---

*Document v1.0 · 2026-07-20 · Maintenir à jour avec les nouvelles compétences.*
