<div align="center">

![Terraform Survivor Banner](docs/assets/banner.svg)

# 🏔️ Terraform Survivor

> Infrastructure as Code meets Survival RPG

A browser-based survival game where **Terraform controls the difficulty**. Demonstrates clean architecture, component design, and IaC principles.

</div>

## 🎮 Play Now

**Live Demo:** https://mark-siazon.github.io/AE3-Terraform_Survivor/

**Author portfolio:** https://www.marksiazon.dev/

## 🚀 Quick Start

```bash
# Play locally (easiest)
python run-game.py
# Opens browser automatically at http://localhost:8000/src/frontend/standalone.html

# Or open directly (no server)
open src/frontend/standalone.html
```

## 🏗️ Terraform Implementation

This project uses **Terraform as Infrastructure as Code** to manage game configuration and deployment:

### How Terraform Controls the Game

Terraform generates `src/frontend/config.js` which controls:

- **Game Difficulty** (easy/normal/hard/extreme)
- **Resource Decay Rates** (hunger, thirst, energy)
- **Starting Resources** (wood, stone, food)
- **Danger Level** (encounter probability)
- **Feature Toggles** (crafting, weather, events)

### Configure Game Difficulty with Terraform

```bash
cd src/infrastructure/terraform

# Initialize Terraform
terraform init

# Apply Easy Mode (Development)
terraform apply -var-file="environments/dev.tfvars" -auto-approve

# Apply Hard Mode (Production)
terraform apply -var-file="environments/prod.tfvars" -auto-approve

# View current configuration
terraform output
```

### Deploy to GitHub Pages

```bash
# 1. Configure with Terraform
terraform apply -var-file="environments/prod.tfvars" -auto-approve

# 2. Commit and push
git add ../../frontend/config.js
git commit -m "Update game config via Terraform"
git push origin main

# 3. GitHub Actions automatically deploys to Pages
```

See [Terraform Deployment Guide](docs/TERRAFORM_DEPLOYMENT.md) for detailed instructions.

## 📁 Structure

```
terraform-survivor/
├── src/
│   ├── frontend/          # Game (HTML, CSS, JS)
│   └── infrastructure/    # Terraform configs
├── docs/
│   ├── guides/            # User docs (4 guides)
│   └── reference/         # Technical docs (2 docs)
└── .github/
    ├── tools/             # Dev server
    └── tests/             # Test files
```

## ⌨️ Controls

**E** Explore | **H** Hunt | **W** Water | **F** Eat | **R** Rest | **C** Craft | **S** Status | **O** Settings | **?** Help

## 🎯 Features

- Survival mechanics (health, hunger, thirst, energy)
- Terraform-controlled difficulty
- **Interactive UI** - Click stats for instant help, click food to eat
- **Smart tooltips** - Shows solutions based on your inventory
- **Auto-save system** with localStorage persistence
- **In-game settings panel** for real-time difficulty adjustment
- **Achievement system** with 9 unlockable achievements
- **Statistics tracking** across all games
- **Notification system** for achievements and events
- Full keyboard support & accessibility (WCAG 2.1 AA)
- Component-based architecture
- No dependencies, no build

## 📚 Documentation

**Getting Started:**

- [Quick Start](docs/guides/QUICKSTART.md) - Get playing in 5 minutes
- [Setup Guide](docs/guides/START_HERE.md) - Installation and setup
- [Deployment](docs/guides/DEPLOYMENT.md) - Deploy to GitHub Pages, Vercel
- [Terraform Deployment](docs/TERRAFORM_DEPLOYMENT.md) - **IaC deployment guide**

**Features:**

- [Complete Feature List](docs/reference/FEATURES.md) - All game features
- [Changelog](CHANGELOG.md) - Version history
- [Quick Reference](docs/guides/QUICK_REFERENCE.md) - Quick commands
- [Interactive Features](docs/guides/INTERACTIVE_FEATURES.md) - UI guide
- [Accessibility](docs/guides/ACCESSIBILITY.md) - Controls & accessibility

**For Developers:**

- [Developer Guide](docs/reference/DEVELOPER_GUIDE.md) - How to extend the game
- [Modular Architecture](docs/reference/MODULAR_ARCHITECTURE.md) - System design
- [Architecture](docs/reference/ARCHITECTURE.md) - Code structure
- [Components](docs/reference/COMPONENTS.md) - Component API reference
- [Visual Improvements](docs/reference/VISUAL_IMPROVEMENTS.md) - UI/UX enhancements
- [Project Summary](docs/reference/PROJECT_COMPLETE.md) - Complete overview

## 🔧 Development

```bash
# Start local server
python run-game.py

# Configure game with Terraform
cd src/infrastructure/terraform
terraform init
terraform apply -var-file="environments/dev.tfvars"

# Deploy changes
git add ../../frontend/config.js
git commit -m "Update config"
git push origin main
```

## 🧪 Testing Terraform Configuration

```bash
# View what would change (dry run)
terraform plan -var-file="environments/prod.tfvars"

# Apply and see outputs
terraform apply -var-file="environments/prod.tfvars"

# Check generated config
cat ../../frontend/config.js

# View deployment info
terraform output
```

## 🎮 How Terraform Integration Works

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Terraform Configuration                   │
│  (src/infrastructure/terraform/)                            │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ variables.tf │  │   main.tf    │  │ outputs.tf   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│         │                  │                  │             │
│         └──────────────────┼──────────────────┘             │
│                            │                                │
│                            ▼                                │
│                  ┌──────────────────┐                       │
│                  │ config.js.tpl    │ (Template)            │
│                  └──────────────────┘                       │
└─────────────────────────┬────────────────────────────────────┘
                          │
                          │ terraform apply
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Generated Configuration File                    │
│  (src/frontend/config.js)                                   │
│                                                              │
│  const CONFIG = {                                           │
│    difficulty: "hard",                                      │
│    gameSettings: {                                          │
│      hungerDecayRate: 3.0,                                  │
│      resourceMultiplier: 0.8,                               │
│      dangerLevel: 0.5                                       │
│    }                                                        │
│  }                                                          │
└─────────────────────────┬────────────────────────────────────┘
                          │
                          │ git push
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              GitHub Actions Workflow                         │
│  (.github/workflows/deploy-pages.yml)                       │
│                                                              │
│  1. Checkout code                                           │
│  2. Upload /src/frontend to GitHub Pages                    │
│  3. Deploy to: mark-siazon.github.io/...                    │
└─────────────────────────┬────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   Live Game (Browser)                        │
│  Loads config.js and applies Terraform-defined settings     │
└─────────────────────────────────────────────────────────────┘
```

### Terraform Variables Control Game Behavior

| Variable              | Effect                  | Easy Mode | Hard Mode |
| --------------------- | ----------------------- | --------- | --------- |
| `hunger_decay_rate`   | How fast you starve     | 1.0x      | 3.0x      |
| `thirst_decay_rate`   | How fast you dehydrate  | 1.5x      | 4.0x      |
| `energy_decay_rate`   | How fast you tire       | 1.0x      | 2.0x      |
| `resource_multiplier` | Gathering efficiency    | 2.0x      | 0.8x      |
| `danger_level`        | Encounter chance        | 10%       | 50%       |
| `crafting_enabled`    | Feature toggle          | ✅        | ✅        |
| `starting_resources`  | Initial wood/stone/food | 10/5/5    | 3/2/1     |

### Environment Files

Edit `src/infrastructure/terraform/environments/*.tfvars` to customize:

- **`dev.tfvars`** - Easy mode for testing
- **`prod.tfvars`** - Hard mode for production
- **`staging.tfvars`** - Create your own custom difficulty

### Why Use Terraform?

1. **Version Control** - Game settings tracked in Git
2. **Reproducibility** - Same config every deployment
3. **Environment Management** - Easy dev/staging/prod separation
4. **Infrastructure as Code** - Demonstrates IaC principles
5. **Automation** - One command updates everything

## 📝 License

MIT

