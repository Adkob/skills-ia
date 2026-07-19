---
name: stitch
description: "Generate and iterate on UI screens, wireframes, mockups, and frontend designs using the Stitch MCP (Google's AI UI generation tool). Use this skill whenever the user asks to: create a UI screen, generate a design mockup, design an app interface, build a wireframe, generate variants of a design, create or apply a design system/theme, edit visual screens with a text prompt, or prototype an app layout. Also trigger when the user mentions 'Stitch', 'screen generation', 'UI generation', 'design system token', 'generate variants', or asks to design any page, dashboard, landing page, form, onboarding flow, or mobile/desktop screen — even if they don't say 'Stitch' explicitly. Always use this skill when UI design output is needed via MCP tools."
compatibility:
  tools:
    - StitchMCP
---

# Stitch — Génération de UI par IA

Stitch est un outil de génération de maquettes UI (Google) accessible via le MCP `StitchMCP`. Il permet de créer des écrans complets (desktop, mobile, tablet) à partir de simples descriptions textuelles, et de les faire évoluer via des prompts itératifs.

---

## Quelle approche utiliser ?

Avant d'appeler le moindre outil, identifie le cas :

- **Je pars de zéro** → Suis le [Workflow complet](#workflow-complet-de-zéro)
- **J'ai déjà un projet Stitch** → Suis [Ajouter un écran à un projet existant](#ajouter-un-écran-à-un-projet-existant)
- **Je veux modifier des écrans existants** → Suis [Édition d'écrans](#édition-décrans)
- **Je veux des variantes de design** → Suis [Génération de variantes](#génération-de-variantes)
- **Je veux créer ou appliquer un design system** → Suis [Design System](#design-system)

---

## Workflow complet (de zéro)

### Étape 1 — Créer un projet

```
Outil : create_project
Paramètre : title (optionnel, mais donne un nom clair)
```

Récupère le `projectId` dans la réponse — tu en auras besoin pour toutes les étapes suivantes.

### Étape 2 — Créer un design system (recommandé)

Avant de générer les écrans, établis la charte graphique pour assurer la cohérence visuelle.

```
Outil : create_design_system
Paramètres obligatoires :
  - designSystem.displayName
  - designSystem.theme.colorMode (LIGHT | DARK)
  - designSystem.theme.headlineFont (ex: INTER, MANROPE, PLUS_JAKARTA_SANS...)
  - designSystem.theme.bodyFont
  - designSystem.theme.roundness (ROUND_FOUR | ROUND_EIGHT | ROUND_TWELVE | ROUND_FULL)
  - designSystem.theme.customColor (hex, ex: "#6C63FF")
Paramètre optionnel :
  - projectId (pour lier au projet)
```

> ⚠️ **Obligatoire** : appelle immédiatement `update_design_system` après `create_design_system` pour activer et afficher le design system.

Récupère l'`assetId` du design system pour l'utiliser lors de la génération d'écrans.

### Étape 3 — Générer les écrans

```
Outil : generate_screen_from_text
Paramètres obligatoires :
  - projectId
  - prompt (description détaillée de l'écran)
Paramètres optionnels :
  - designSystem (format: "assets/{assetId}") — toujours inclure pour la cohérence
  - deviceType (MOBILE | DESKTOP | TABLET | AGNOSTIC)
  - modelId (GEMINI_3_1_PRO recommandé)
```

> ⚠️ **Important** : cet outil peut prendre plusieurs minutes. Ne JAMAIS retenter si timeout.  
> Si timeout → appeler `get_screen` toutes les 30 secondes jusqu'à 10 fois.

> 💡 Si `output_components` contient des suggestions (ex: "Yes, make them all"), présente-les à l'utilisateur. S'il en accepte une, rappelle `generate_screen_from_text` avec ce texte comme `prompt`.

---

## Ajouter un écran à un projet existant

1. Lister les projets : `list_projects`
2. Récupérer le projet cible : `get_project` → noter `projectId` et `designSystem`
3. Lister les écrans existants : `list_screens` (pour context)
4. Générer le nouvel écran : `generate_screen_from_text` avec le `projectId` et le `designSystem` existant

---

## Édition d'écrans

Pour modifier des écrans existants avec un prompt texte :

```
Outil : edit_screens
Paramètres obligatoires :
  - projectId
  - selectedScreenIds (tableau d'IDs d'écrans, sans le préfixe "screens/")
  - prompt (description des modifications à apporter)
Paramètres optionnels :
  - deviceType
  - modelId
```

> ⚠️ Même règle : cet outil peut prendre plusieurs minutes. Ne JAMAIS retenter si timeout.

**Pour obtenir les IDs d'écrans** : appeller `list_screens` avec le `projectId`.

---

## Génération de variantes

Pour explorer des alternatives de design à partir d'un écran existant :

```
Outil : generate_variants
Paramètres obligatoires :
  - projectId
  - selectedScreenIds (1 ou plusieurs IDs d'écrans)
  - prompt (direction créative pour les variantes)
  - variantOptions :
      - variantCount (1-5, défaut 3)
      - creativeRange (REFINE | EXPLORE | REIMAGINE)
      - aspects (LAYOUT | COLOR_SCHEME | IMAGES | TEXT_FONT | TEXT_CONTENT)
```

**Guide `creativeRange`** :
| Valeur | Usage |
|--------|-------|
| `REFINE` | Retouches subtiles, proche de l'original |
| `EXPLORE` | Exploration équilibrée (défaut) |
| `REIMAGINE` | Refonte radicale |

---

## Design System

### Créer depuis un fichier DESIGN.md

Si l'utilisateur fournit un fichier `.md` décrivant son design system :

1. Encoder le contenu en base64 : `base64 -w 0 design.md`
2. Uploader : `upload_design_md` (projectId + designMdBase64)
3. Créer le design system : `create_design_system_from_design_md` immédiatement après

### Appliquer un design system à des écrans existants

```
Outil : apply_design_system
Paramètres :
  - projectId
  - assetId (ID du design system, via list_design_systems)
  - selectedScreenInstances (instances d'écrans depuis get_project)
```

> ⚠️ Utilise les **instance IDs** (pas les source screen IDs) — disponibles via `get_project`.

### Lister les design systems disponibles

```
Outil : list_design_systems
```

Utile pour réutiliser un design system existant sur un nouveau projet.

---

## Outils de consultation (lecture seule)

| Outil | Usage |
|-------|-------|
| `list_projects` | Lister tous les projets Stitch de l'utilisateur |
| `get_project` | Détails d'un projet (écrans, design system, instances) |
| `list_screens` | Lister les écrans d'un projet |
| `get_screen` | Détails et statut d'un écran (utile après timeout) |
| `list_design_systems` | Lister les design systems disponibles |

---

## Bonnes pratiques de prompting pour Stitch

Un bon prompt de génération d'écran contient :
- **Le type de page** : dashboard admin, landing page SaaS, onboarding, formulaire...
- **Le contexte produit** : "pour une app de gestion de tâches", "pour un outil B2B"
- **Le style souhaité** : moderne, minimaliste, glassmorphism, coloré...
- **Les éléments clés** : navigation, cards, graphiques, formulaires, CTA...
- **Le device** : desktop 1440px, mobile iOS, tablet...

**Exemple de prompt efficace** :
> "Dashboard admin pour une app SaaS analytics. Sidebar de navigation à gauche avec icônes. Header avec barre de recherche et avatar. Zone principale avec 4 KPI cards en grid (utilisateurs, revenus, taux de conversion, sessions). Un graphique en courbes pour l'évolution des revenus sur 30 jours. Tableau des dernières transactions. Style sombre, épuré, accent violet (#6C63FF)."

---

## Cas limites et gestion d'erreurs

- **Timeout sur generate/edit** : Ne jamais retenter. Appeler `get_screen` toutes les 30s (max 10 fois).
- **Connection error** : La génération peut continuer côté serveur. Vérifier avec `get_screen` après quelques secondes.
- **Design system requis** : Toujours passer le `designSystem` à `generate_screen_from_text` pour la cohérence visuelle entre les écrans.
- **IDs sans préfixe** : Tous les IDs passés aux outils doivent être sans préfixe (`projects/`, `screens/`, `assets/`).
