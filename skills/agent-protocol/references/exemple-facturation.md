# Annexe — Exemple Bout-en-Bout Multi-Agents (SaaS de facturation)

> Illustre l'enchaînement Jalons A→F avec deux environnements (Claude pour la planification, Antigravity/Gemini pour la construction visuelle), et la couche `execution/`+`directives/` pour toute intégration récurrente (Supabase, exports).

1. **Jalon A/B (Claude)** : brief + plan d'implémentation détaillé (dashboard factures/stats, création facture avec TVA 18% FCFA, clients, statuts, paramètres entreprise) sur Next.js 14 + Supabase + Tailwind, déploiement Vercel. Flux validé : pages connectées (captures d'inspiration) → interactivité données locales → Supabase+tests → auth → landing → E2E+déploiement.
2. **Jalon D/E (Antigravity/Gemini)** : à partir du plan + captures Dribbble, construire d'abord Dashboard+sidebar (données fictives, FCFA, dates jj/mm/aaaa, badges statut colorés, responsive), valider, puis enchaîner Créer facture / Liste factures / Détail facture / Clients en gardant le même style.
3. **Landing page dédiée** (`landing-cinematique` adapté) : styliser depuis une capture d'inspiration sans copier le contenu — hero problème/solution, 3 pain points, 4 fonctionnalités, 3 étapes, témoignages, tarification (Gratuit/Pro 5000 FCFA/Business 15000 FCFA), CTA final, footer.
4. **Jalon F** : `audit-securite-vibe-code` (RLS Supabase, `auth.uid()`, validation serveur des montants/TVA) avant mise en production.
