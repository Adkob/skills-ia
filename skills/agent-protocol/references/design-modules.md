# Modules de Design Internes (fallback sans dépendance externe)

> À utiliser au Jalon D quand Claude Design / `stitch` / `design-system` ne sont pas disponibles, ou que le type de projet correspond exactement à l'un de ces modules. Socle commun aux modules 8.1/8.2 : overlay de bruit SVG (`feTurbulence` 0.05), rayons `rounded-[2rem]→[3rem]` partout, boutons magnétiques `scale(1.03)` + `cubic-bezier(0.25,0.46,0.45,0.94)`, liens `translateY(-1px)` au hover, animations `gsap.context()`+`ctx.revert()` (stagger 0.08 texte/0.15 cartes), stack React 19 + Tailwind 3.4 + GSAP3/ScrollTrigger + Lucide, vraies images Unsplash (jamais de placeholder gris). Directive commune : *"Construire un instrument digital, pas un site web — éradiquer tout pattern générique d'IA."*

## 8.1 — `landing-cinematique`
Flux : poser en un seul appel → (1) nom marque + objectif · (2) preset esthétique · (3) 3 arguments de vente · (4) CTA principal — puis construire sans discuter.

| Preset | Palette (Primaire/Accent/Fond/Texte) | Typo (titres/dramatique/data) | Ambiance |
|---|---|---|---|
| Tech Organique | Mousse #2E4036 / Argile #CC5833 / Crème #F2F0E9 / Charbon #1A1A1A | Plus Jakarta Sans+Outfit / Cormorant Garamond It. / IBM Plex Mono | Forêt, labo bio |
| Luxe de Minuit | Obsidienne #0D0D12 / Champagne #C9A84C / Ivoire #FAF8F5 / Ardoise #2A2A35 | Inter / Playfair Display It. / JetBrains Mono | Marbre, or |
| Signal Brutaliste | Papier #E8E4DD / Rouge #E63B2E / Blanc cassé #F5F3EE / Noir #111111 | Space Grotesk / DM Serif Display It. / Space Mono | Béton, industriel |
| Clinique Vapor | Vide #0A0A14 / Plasma #7B61FF / Fantôme #F0EFF4 / Graphite #18181B | Sora / Instrument Serif It. / Fira Code | Bioluminescence, néon |

Architecture figée (contenu/couleurs adaptables, structure non) : **Navbar** pilule flottante morphante (transparent→blur au scroll) · **Hero** 100dvh image+overlay, titre 2 parties (sans-gras + serif italique 3-5x) · **Fonctionnalités** 3 cartes-micro-interfaces (mélangeur diagnostique cyclique / machine à écrire télémétrie / planificateur curseur animé) · **Philosophie** 2 déclarations contrastées sur fond sombre + parallax · **Protocole** 3 cartes sticky empilées (ScrollTrigger pin) avec animation SVG unique chacune · **Tarification** 3 niveaux, carte du milieu mise en avant · **Footer** sombre `rounded-t-[4rem]` + statut "Système Opérationnel".

## 8.2 — `cv-cinematique`
Flux : (1) nom + titre pro · (2) preset esthétique · (3) parcours en 2-3 phrases · (4) 3 expériences + 5 compétences.

| Preset | Palette | Typo | Ambiance |
|---|---|---|---|
| Architecte Minimal | Encre #1C1C1E / Corail #E8634A / Neige #FAFAFA / Graphite #2D2D2D | Plus Jakarta Sans / Cormorant Garamond It. / IBM Plex Mono | Espaces épurés |
| Nocturne Prestige | Charbon #0F0F13 / Or #D4A843 / Crème #F5F3EE / Ardoise #1E1E26 | Inter / Playfair Display It. / JetBrains Mono | Intérieurs sombres, bois/cuir |
| Signal Brut | Papier #E8E4DD / Bleu #2563EB / Blanc cassé #F5F3EE / Noir #111111 | Space Grotesk / DM Serif Display It. / Space Mono | Bureaux, écrans |
| Aura Digitale | Vide #0A0A14 / Violet #7B61FF / Fantôme #F0EFF4 / Graphite #18181B | Sora / Instrument Serif It. / Fira Code | Gradients sombres |

Architecture figée : **Navbar** signature flottante · **Hero** centré (photo cercle + nom massif + titre serif italique + 3 stats mono + 2 CTA) · **À propos** 2 colonnes séparées par ligne accent · **Expérience** timeline verticale alternée avec point pulsant · **Compétences** radar SVG animé / grille de maîtrise % animé / tags pondérés (choisir le plus adapté) · **Formation** cartes empilées fond sombre · **Contact** icônes+liens stagger + CTA "Télécharger CV" (`<a download>`, PDF placeholder à remplacer) · **Footer** minimaliste + indicateur "En ligne".

## 8.3 — `saas-designer` (skill générale SaaS/dashboard)
```yaml
name: saas-designer
description: Design premium, pixel-perfect SaaS interfaces (dashboards, landing,
  auth, forms, lists). Analyse le codebase existant avant toute décision de design.
```
**Flux obligatoire** : **Étape 1 — analyser le codebase en premier** (structure, `tailwind.config.*`/`globals.css`, composants existants, pages, `package.json`, assets/fonts) → **Étape 2 — déterminer le mode** :

| Mode | Contexte | Action |
|---|---|---|
| A | Design system existant | Travailler dedans, raffiner, ajouter micro-interactions manquantes, ne rien casser |
| B | Design incohérent/générique | Créer un système cohérent en gardant ce qui est bon, refactorer progressivement |
| C | Rien n'existe | Poser en un appel : nom+objectif / preset esthétique / pages principales / captures d'inspiration ? / CTA |

→ **Étape 3 — construire** sans discussion préalable ; ajuster ensuite. Si captures fournies : extraire les patterns (ombres, rayons, densité, espace blanc) et produire mieux qu'une simple imitation.

**Presets (Mode C)** :
| Preset | Fond/Cartes/Hover | Accent/Succès/Warning/Erreur | Fonts | Effet |
|---|---|---|---|---|
| Nuit Professionnelle | #0F1117/#1A1D27/#242833 | #6C5CE7/#00D68F/#FFB800/#FF4757 | Inter/Inter/JetBrains Mono | Glassmorphism |
| Lumière Épurée | #FAFBFC/#FFFFFF/#F3F4F6 | #2563EB/#059669/#D97706/#DC2626 | Plus Jakarta Sans/idem/IBM Plex Mono | Ombres douces |
| Néon Opérationnel | #09090B/#18181B/#27272A | #22D3EE/#4ADE80/#FACC15/#F87171 | Sora/Inter/Fira Code | Glow accent |
| Afrique Premium | #FFFBF5/#FFFFFF/#FFF7ED | #EA580C/#16A34A/#CA8A04/#DC2626 | Plus Jakarta Sans/DM Sans/Space Mono | Ombres chaudes, `rounded-2xl` |

**Règles absolues** : jamais de fond plat (ombre/bordure/glassmorphism/gradient), 1 seul système de rayons cohérent · micro-interactions obligatoires (boutons scale+span glissant, cartes translateY(-2px), inputs focus ring, modals fade+scale, skeleton shimmer à la forme du contenu) · stagger reveal + compteurs animés + scroll fade-up · hiérarchie typo nette, tracking serré titres, monospace pour data · spacing en système 8px, sidebar 240-280px fixe, contenu max-width 1200-1400px · 4 états visuels par élément interactif (default/hover/active/disabled).
**Composants de référence** : Sidebar (actif = fond accent/10+barre 3px, collapse hamburger mobile) · Navbar sticky · Cartes de stats (icône+valeur mono+variation%) · Tableaux (header sticky, badges statut pastel+point) · Formulaires (labels au-dessus, validation inline) · Modals (backdrop blur, fade+scale) · Auth (split 60/40 ou centré) · Landing (navbar morphante, hero 100vh, features en micro-UI) · Empty state (illustration+CTA).
**Hiérarchie de décision** : 1) codebase existant a la réponse → l'utiliser · 2) capture d'inspiration → extraire et adapter · 3) preset défini → le suivre · 4) sinon → décision experte documentée en commentaire de code.
