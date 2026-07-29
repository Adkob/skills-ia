---
name: createur-agents
description: Crée, met à jour et renforce les fiches agents Claude Code (fichiers .claude/agents/*.md). À utiliser systématiquement dès que l'utilisateur veut créer un nouvel agent, modifier le rôle ou les compétences d'un agent existant, ajouter des skills à un agent, écrire une fiche de poste départementale, ou auditer la qualité d'un agent existant. Se déclenche aussi sur "fiche de poste agent", "renforce l'agent X", "mets à jour l'agent Y", "crée un département Z".
---

# Créateur d'Agents

Une skill pour concevoir, rédiger, améliorer et auditer des fiches agents Claude Code (`.claude/agents/*.md`).

---

## Pourquoi cette skill existe

Un fichier agent mal conçu produit un agent qui rate ses cibles : trop large dans sa description (il se déclenche quand il ne faut pas), trop vague dans son rôle (il improvise), ou sans les bonnes skills (il travaille à mains nues). Cette skill garantit une conception rigoureuse à chaque fois.

---

## Étape 1 — Cerner l'intention

Avant de rédiger, pose les questions suivantes (une seule si le contexte est déjà clair) :

1. **Quel est le périmètre exact de cet agent ?** (département, pôle, rôle principal)
2. **Quand doit-il se déclencher ?** (phrases typiques, contextes d'usage)
3. **Quels outils et skills doit-il avoir ?** (ou laisser la skill faire l'audit)
4. **Y a-t-il des règles non négociables ?** (ton, interdits, format de sortie)

Si l'agent cible existe déjà, lis son fichier avant de proposer des modifications.

---

## Étape 2 — Structure obligatoire d'un fichier agent

Chaque fichier `.claude/agents/<name>.md` suit cette structure :

```markdown
---
name: <slug-kebab-case, max 64 chars>
description: <déclencheur précis et insistant, max 200 chars>
tools: <liste des outils séparés par des virgules>
skills: <liste des skills séparées par des virgules, ou omis si aucune>
model: <sonnet | opus | haiku>
permissionMode: <default | acceptEdits | bypassPermissions>
memory: <project | user | omis>
color: <couleur en anglais>
---

# <Nom de l'agent>, <Titre court du département>

<Persona : qui est cet agent, pour qui il travaille, quel est son niveau d'exigence>

---

## Contexte

<Ce que l'agent doit savoir sur la situation, les objectifs, les contraintes>

---

## Responsabilités

<Liste structurée des tâches, idéalement en sous-sections par domaine>

---

## Règles non négociables

<Interdits absolus, règles de ton, règles de format, règles de sécurité>

---

## Format de progression / de livraison

<Comment l'agent rend compte, dans quel format, avec quelle cadence>
```

### Valeurs recommandées par type d'agent

| Type d'agent | Model | PermissionMode | Memory |
|---|---|---|---|
| Orchestrateur / CEO | opus | default | project |
| Agent opérationnel (rédaction, conseil) | sonnet | default | project |
| Agent technique (code, dev) | sonnet | acceptEdits | project |
| Agent de recherche / veille | sonnet | default | omis |

---

## Étape 3 — Choisir les bons outils et skills

### Outils disponibles (tools)

| Outil | Quand l'inclure |
|---|---|
| `Read, Write, Edit` | Toujours pour les agents qui produisent des documents |
| `Grep, Glob` | Agents qui cherchent dans des fichiers du projet |
| `WebSearch, WebFetch` | Agents qui font de la veille ou de la recherche |
| `Bash` | Agents techniques uniquement (dev, scripts) |
| `Agent` | Orchestrateurs uniquement (pour déléguer à d'autres agents) |

### Skills recommandées par département

| Département | Skills recommandées |
|---|---|
| Commerce & Ventes | `docx`, `pdf`, `xlsx` |
| Marketing & Communication | `docx`, `pdf`, `pptx` |
| Dev & Tech | `docx`, `pdf`, `full-output-enforcement`, `webapp-testing`, `modern-web-guidance`, `frontend-design` |
| Conseil & Missions | `docx`, `pdf`, `pptx`, `xlsx` |
| Admin & Opérations | `docx`, `pdf`, `xlsx` |
| R&D & Innovation | `claude-api`, `mcp-builder`, `skill-creator` |
| Carrière & Candidatures | `docx`, `pdf` |
| Marque Personnelle | `docx`, `pdf` |
| Réseau & Communautés | `pptx`, `slides` |
| Savoirs & Présentations | `docx`, `pdf`, `pptx` |
| Veille & Opportunités | `docx`, `pdf` |

---

## Étape 4 — Rédiger la description (le levier critique)

La description est le mécanisme principal de déclenchement. Elle doit :
- Nommer le département et le rôle clairement
- Lister les situations typiques d'usage (avec "À utiliser quand...")
- Être légèrement insistante pour ne pas être ignorée
- Rester sous 200 caractères

**Mauvais exemple :**
> "Agent de commerce."

**Bon exemple :**
> "Département Commerce & Ventes. Gère les offres commerciales, devis et prospection. À utiliser quand l'utilisateur veut préparer une offre, calculer un devis, analyser un prospect ou réfléchir à sa stratégie commerciale."

---

## Étape 5 — Audit d'un agent existant

Quand l'utilisateur veut améliorer un agent existant, applique cette grille :

```
## Audit — <nom de l'agent>

| Critère | Statut | Observation |
|---|---|---|
| Description déclenchante et précise | ✓ / ✗ | |
| Frontmatter complet (tools, skills, model, color) | ✓ / ✗ | |
| Persona clair et niveau d'exigence défini | ✓ / ✗ | |
| Responsabilités structurées par domaine | ✓ / ✗ | |
| Skills suffisantes pour le périmètre | ✓ / ✗ | |
| Règles non négociables explicites | ✓ / ✗ | |
| Règle anti-fabrication si données sensibles | ✓ / ✗ | |
| Format de livraison défini | ✓ / ✗ | |

### Skills manquantes recommandées
<liste avec justification>

### Priorités de révision
<top 3 points à corriger>
```

---

## Étape 6 — Vérification finale avant livraison

Avant de livrer le fichier agent, vérifie :

- [ ] Le `name` est en kebab-case, sans espace, sans majuscule
- [ ] La `description` déclenche sur les bons cas et pas sur les mauvais
- [ ] Les `tools` sont limités au strict nécessaire (principe de moindre privilège)
- [ ] Les `skills` couvrent tous les types de livrables attendus
- [ ] Le `model` est adapté à la complexité du rôle
- [ ] La `color` est définie (aide à l'identification visuelle)
- [ ] Le corps du fichier suit la structure en 5 sections
- [ ] Les règles non négociables sont explicites et justifiées
- [ ] Pas de tirets longs (em dashes) dans le contenu

---

## Règles de cette skill

- Ne jamais créer un agent sans avoir cerné son périmètre exact. Un agent trop large devient inutilisable.
- Ne pas dupliquer des agents qui existent déjà. Vérifier d'abord dans `.claude/agents/`.
- Si l'agent cible est partagé entre deux pôles, le documenter explicitement dans sa description et ses règles.
- Proposer toujours l'audit avant une réécriture complète d'un agent existant.
- Mettre à jour `CLAUDE.md` après création ou modification significative d'un agent.
