# 🔮 Contributing to ExpenseOracle

Thank you for seeking to enhance the Oracle's powers! This document guides you through contributing to the **ExpenseOracle** project.

## 🌟 The Oracle's Principles

1. **Privacy is Sacred**: No external data transmission, ever
2. **Local-First**: All divinations happen on your device
3. **Open Visions**: Transparent, auditable code
4. **Accessible Wisdom**: Free for all seekers

## 🚀 Setting Up Your Sanctuary

### Prerequisites
- Python 3.11+
- Ollama installed locally
- Git

### Development Ritual

``bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/expenseoracle.git
cd expenseoracle

# Create your virtual sanctuary
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install the Oracle's tools
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks (magical wards)
pre-commit install

# Verify the Oracle responds
pytest tests/
``

## 🌿 Branch Naming Convention

ExpenseOracle follows structured branch naming.

Format: `type/scope/short-description`


| Type | Purpose | Example |
|------|---------|---------|
| `features/` | New features, enhancements, capabilities | `features/configs/repo-configuration` |
| `tests/` | Test suites, testing infrastructure | `tests/frontend/data-viz-testing` |
| `docs/` | Documentation updates, README, wiki | `docs/readme-updated` |
| `bugfix/` | Bug fixes, curse removals | `bugfix/backend/anomaly-detection-fix` |
| `hotfix/` | Critical production fixes | `hotfix/security/dependency-patch` |
| `refactor/` | Code restructuring, no feature changes | `refactor/models/clean-architecture` |
| `chore/` | Maintenance, dependencies, CI/CD | `chore/deps/update-ollama` |
| `release/` | Version releases | `release/v1.2.0` |

### 🎯 Scope Categories

| Scope | Description | Used With |
|-------|-------------|-----------|
| `configs/` | Configuration, setup, infrastructure | `features/`, `chore/` |
| `frontend/` | UI, Chainlit interface, visualizations | `features/`, `tests/`, `bugfix/` |
| `backend/` | API, database, models | `features/`, `tests/`, `bugfix/` |
| `rag/` | RAG pipeline, embeddings, vector store | `features/`, `refactor/` |
| `ml/` | Machine learning, analytics, predictions | `features/`, `tests/` |
| `models/` | Data models, schemas | `features/`, `refactor/` |
| `utils/` | Utilities, helpers, parsers | `features/`, `bugfix/` |
| `security/` | Security fixes, privacy enhancements | `features/`, `hotfix/`, `bugfix/` |
| `deps/` | Dependencies, requirements | `chore/`, `features/` |
| `ci/` | GitHub Actions, workflows | `chore/`, `features/` |
| `docs/` | Documentation, README, wiki | `docs/`, `features/docs/` |
| `performance/` | Speed, memory optimizations | `features/`, `refactor/` |

### 📝 Description Rules

- **Format**: Lowercase, hyphen-separated, no spaces
- **Length**: Maximum 50 characters for the description part
- **Clarity**: Descriptive but concise
- **Tense**: Present tense (e.g., `add-feature`, not `added-feature`)

### ✅ Valid Examples

### Features
- `features/configs/repo-configuration`
- `features/frontend/ui-design`
- `features/backend/database-configuration`
- `features/rag/embedding-optimization`
- `features/ml/advanced-anomaly-detection`
- `features/security/privacy-audit-logging`
- `features/performance/query-caching`

### Tests
- `tests/frontend/data-viz-testing`
- `tests/backend/expense-manager-unit`
- `tests/rag/retrieval-accuracy`
- `tests/ml/prediction-validation`
- `tests/security/privacy-compliance`

### Documentation

- `docs/readme-updated`
- `docs/api-reference-created`
- `docs/architecture-diagrams`
- `docs/wiki-created`
- `docs/contributing-guide`

### Chores/Maintenance
- `chore/deps/update-llama-index`
- `chore/ci/add-python-312`
- `chore/configs/pre-commit-hooks`
- `chore/security/dependency-audit`

### Bug Fixes

- `bugfix/frontend/chart-rendering-fix`
- `bugfix/backend/duplicate-transaction`
- `bugfix/rag/embedding-timeout`
- `bugfix/ml/anomaly-false-positive`


### Refactoring
- `refactor/models/clean-architecture`
- `refactor/utils/bank-parser-abc`
- `refactor/tests/pytest-fixtures`

### Hotfixes

hotfix/security/sqlite-injection-patch

hotfix/backend/data-corruption-fix

### ❌ Invalid Examples

- `feature-new-thing`: Missing type/scope structure

- `features-new-ui`: Missing scope separator
- 
- `features/NEW-UI`: Uppercase not allowed

- `features/ui design`: Spaces not allowed

- `features/frontend/ui-design-with-very-long-description-exceeding-fifty-chars`: Too long

- `feat/ui`: Wrong type prefix

- `feature/configs/test`:  Wrong type (should be features/)

- `test/frontend/data`: Wrong type (should be tests/)

- `doc/readme`: Wrong type (should be docs/)

### 🔍 Validation

Before pushing, verify your branch name:

```bash
# Check current branch
git branch --show-current

# Should match: ^(features|tests|docs|bugfix|hotfix|refactor|chore|release)/[a-z0-9-]+/[a-z0-9-]{1,50}$

# Example validation script
./scripts/validate-branch-name.sh
```