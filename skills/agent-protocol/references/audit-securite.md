# Module — Audit de Sécurité Vibe-Code (`audit-securite-vibe-code`)

> À invoquer au Jalon F pour tout projet SaaS/Fullstack/Automatisation manipulant secrets, DB ou auth. Conçu pour l'angle mort typique du code généré par IA.

**Méthodologie** : Passe 1 — lire toute la codebase, modéliser l'architecture (framework/DB/auth/API/déploiement), tracer chaque point d'entrée et le flux de données. Passe 2 — verdict individuel par item, jamais groupé : ✅ PASSE (fichier/ligne) · ❌ ÉCHOUÉ (documenter) · ⚠ PARTIEL (ce qui manque) · ⬚ N/A (pourquoi).

**Format par conclusion ❌** : Sévérité (CRITIQUE/HAUTE/MOYENNE/BASSE) · Catégorie · Emplacement (fichier:ligne) · CWE · Ce qui ne va pas · Pourquoi c'est important · Code vulnérable · La correction · Effort estimé (min).

**Checklist condensée** :
| Domaine | Points de contrôle clés |
|---|---|
| **Secrets/env** | Secrets en dur (grep `sk_live_`, `Bearer`, `eyJ`, `ghp_`, `xoxb-`, `AKIA`...) · couverture `.gitignore` + historique git · préfixes publics (`NEXT_PUBLIC_`/`VITE_`) sur clés serveur · fuites console/erreurs · source maps en prod · validation au démarrage |
| **Base de données** | RLS activé sur chaque table · policies SELECT/INSERT existantes · `WITH CHECK` sur INSERT/UPDATE · identité via `auth.uid()` (jamais `user_metadata`) · `service_role` jamais côté client · policies buckets storage · injection SQL sur requêtes brutes · fonctions `SECURITY DEFINER` |
| **Auth/sessions** | Middleware d'auth + matcher complet · refus par défaut (liste blanche) · `getUser()` vs `getSession()` · callback OAuth sécurisé (state anti-CSRF) · session en cookie `httpOnly` (jamais localStorage) · chaque route API protégée · reset mdp : tokens expirables/usage unique |
| **Validation serveur** | Schéma (Zod/Yup...) sur toutes les routes · identité dérivée de la session (jamais du body) · anti-XSS (`dangerouslySetInnerHTML`...) · mutations en POST/PUT/PATCH/DELETE · erreurs sans fuite interne · signature webhook vérifiée |
| **Dépendances** | `npm/pnpm audit` par sévérité · packages hallucinés · lockfile commité · packages obsolètes/CVE · dépendances inutilisées |
| **Rate limiting** | Routes API payantes limitées · endpoints auth limités (anti brute-force) · stockage fiable (Redis), pas en mémoire |
| **CORS** | Pas de `Access-Control-Allow-Origin: *` sur endpoints sensibles · `Allow-Credentials` jamais avec wildcard |
| **Upload fichiers** | Validation MIME+taille serveur · contrôles d'accès public/privé différenciés · non-exécutable |

**Rapport final** : 1) Posture globale (🔴Critique/🟠À améliorer/🟡Acceptable/🟢Solide) + résumé exécutif · 2) Conclusions Critiques/Hautes consolidées · 3) Victoires rapides (<10 min) · 4) Plan de remédiation priorisé (sévérité puis effort, temps estimé) · 5) Ce qui est déjà bien fait · 6) Résumé compact checklist (`1.1 ✅ 1.2 ❌ ...`).

Priorité aux vulnérabilités réelles/exploitables sur les préoccupations théoriques ; incertitude → ⚠ PARTIEL en expliquant ce qu'il faudrait vérifier.
