# skills-ia

Dépôt de compétences (skills) pour agents IA — compatible Google Antigravity (Gemini), Claude, et autres environnements supportant le format SKILL.md.

Ce dépôt suit l'architecture à 3 couches décrite dans [AGENTS.md](./AGENTS.md) :
- **Couche 1 — Directives** : SOPs Markdown dans `directives/`
- **Couche 2 — Orchestration** : L'agent IA (toi)
- **Couche 3 — Exécution** : Scripts Python dans `execution/`

## Structure

```
skills-ia/
├── AGENTS.md           # Instructions pour agents IA (tous environnements)
├── CLAUDE.md           # Alias AGENTS.md pour Claude
├── GEMINI.md           # Alias AGENTS.md pour Gemini/Antigravity
├── directives/         # Procédures opérationnelles (SOPs)
├── execution/          # Scripts Python déterministes
└── skills/             # 83 compétences globales installées
    ├── brainstorming/
    ├── planification/
    ├── ui-ux-pro-max/
    ├── remotion-best-practices/
    └── ...
```

## Compétences disponibles (83)

### 🧠 Workflow & Stratégie Agent
| Skill | Description |
|-------|-------------|
| `brainstorming` | Exploration des besoins avant toute implémentation |
| `planification` | Plans d'implémentation multi-étapes |
| `skill-creator` | Créer et améliorer des compétences |
| `skill-repair` | Réparer des skills cassés |
| `accidental-data-loss-prevention` | Prévention de perte de données accidentelle |

### 🎨 Design & UI/UX
| Skill | Description |
|-------|-------------|
| `ui-ux-pro-max` | Design UI/UX avancé |
| `banner-design` | Création de bannières |
| `brand` | Identité de marque |
| `brand-guidelines` | Charte graphique Anthropic |
| `canvas-design` | Art visuel statique |
| `design` | Système de design complet |
| `design-system` | Tokens et composants |
| `frontend-design` | Design frontend distinctif |
| `slides` | Présentations HTML |
| `theme-factory` | Thèmes visuels |
| `ui-styling` | Styling shadcn/Tailwind |
| `algorithmic-art` | Art génératif p5.js |

### 🎬 Vidéo & Médias
| Skill | Description |
|-------|-------------|
| `remotion-best-practices` | Meilleures pratiques Remotion (React video) |
| `slack-gif-creator` | GIFs animés optimisés Slack |

### 📄 Documents & Productivité
| Skill | Description |
|-------|-------------|
| `docx` | Fichiers Word .docx |
| `pdf` | Manipulation de PDFs |
| `pptx` | Présentations PowerPoint |
| `xlsx` | Tableurs Excel |
| `doc-coauthoring` | Co-rédaction de documentation |
| `internal-comms` | Communications internes |

### 🤖 Développement & IA
| Skill | Description |
|-------|-------------|
| `claude-api` | API Anthropic / Claude SDK |
| `mcp-builder` | Création de serveurs MCP |
| `web-artifacts-builder` | Artefacts web React complexes |
| `webapp-testing` | Tests d'applications web (Playwright) |

### ☁️ Google Cloud Platform
| Skill | Description |
|-------|-------------|
| `bigquery` | Requêtes et optimisation BigQuery |
| `bigquery-data-transfer-service` | Pipelines d'ingestion DTS |
| `building-data-apps` | Applications de données (React/Streamlit) |
| `data-autocleaning` | Nettoyage automatique de données |
| `dataform-bigquery` | Pipelines Dataform ELT |
| `dbt-bigquery` | Pipelines dbt pour BigQuery |
| `discovering-gcp-data-assets` | Découverte d'assets GCP |
| `federate-lakehouse-catalog` | Fédération Iceberg REST Catalogs |
| `firestore-data` | Opérations Firestore NoSQL |
| `gcloud-auth-verification` | Authentification Google Cloud ADC |
| `gcp-composer-troubleshooting` | Dépannage Cloud Composer/Airflow |
| `gcp-data-pipelines` | Orchestration de pipelines données |
| `gcp-dataflow` | Pipelines Apache Beam sur Dataflow |
| `gcp-managed-airflow-migrations` | Migration Airflow DAGs |
| `gcp-pipeline-orchestration` | Orchestration via Cloud Composer |
| `gcp-pipeline-resource-provisioning` | Provisionnement déclaratif GCP |
| `gcp-spark` | Spark sur Dataproc |
| `gcs-security-assessment` | Audit sécurité GCS |
| `managing-python-dependencies` | Gestion des dépendances Python |
| `ml-best-practices` | Meilleures pratiques ML/Data |
| `notebook-guidance` | Notebooks Jupyter / BigQuery |
| `spanner-data` | Données Cloud Spanner |

### 🛢️ AlloyDB & Cloud SQL
Plus de 20 compétences couvrant AlloyDB Omni, AlloyDB Postgres, Cloud SQL MySQL/Postgres/SQL Server — admin, data, health, monitor, replication, optimize, lifecycle.

## Installation

```bash
git clone https://github.com/Adkob/skills-ia.git
```

Pour utiliser les skills globalement dans Antigravity/Gemini, copier le contenu de `skills/` dans `~/.gemini/config/skills/`.

## Licence

MIT
