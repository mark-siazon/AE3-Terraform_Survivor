# 🏗️ Terraform Deployment Guide

This project uses Terraform to configure game difficulty and settings for GitHub Pages deployment.

## ✅ Setup Complete

Your game is configured with Terraform and deployed to:
**https://mark-siazon.github.io/AE3-Terraform_Survivor/**

## 🎮 How It Works

Terraform generates `src/frontend/config.js` based on environment variables, controlling:

- Game difficulty (easy/normal/hard/extreme)
- Resource decay rates
- Starting resources
- Feature toggles

## 📋 Quick Commands

### Deploy Production (Hard Mode)

```bash
cd src/infrastructure/terraform
terraform apply -var-file="environments/prod.tfvars" -auto-approve
git add ../../frontend/config.js
git commit -m "Update to hard mode via Terraform"
git push origin main
```

### Deploy Development (Easy Mode)

```bash
cd src/infrastructure/terraform
terraform apply -var-file="environments/dev.tfvars" -auto-approve
git add ../../frontend/config.js
git commit -m "Update to easy mode via Terraform"
git push origin main
```

### View Current Configuration

```bash
cd src/infrastructure/terraform
terraform output
```

## 🎯 Available Environments

### Development (Easy Mode)

- **File**: `environments/dev.tfvars`
- **Difficulty**: Easy
- **Starting Resources**: 10 wood, 5 stone, 5 food
- **Hunger Decay**: 1.0 (slow)
- **Resource Multiplier**: 2.0 (double resources)
- **Danger Level**: 0.1 (low)

### Production (Hard Mode)

- **File**: `environments/prod.tfvars`
- **Difficulty**: Hard
- **Starting Resources**: 3 wood, 2 stone, 1 food
- **Hunger Decay**: 3.0 (fast)
- **Resource Multiplier**: 0.8 (fewer resources)
- **Danger Level**: 0.5 (high)

### Staging (Normal Mode)

- **File**: `environments/staging.tfvars`
- Create this file to add a normal difficulty tier

## 🔧 Customizing Difficulty

Edit the `.tfvars` files to create custom difficulty levels:

```hcl
environment = "custom"
difficulty  = "extreme"

starting_resources = {
  wood  = 1
  stone = 1
  food  = 0
}

game_settings = {
  hunger_decay_rate   = 5.0
  thirst_decay_rate   = 6.0
  energy_decay_rate   = 3.0
  resource_multiplier = 0.5
  danger_level        = 0.8
}

features = {
  crafting_enabled = true
  weather_events   = true
  random_events    = true
}

game_version = "1.0.0-extreme"
```

## 📊 Terraform Outputs

After running `terraform apply`, you'll see:

- **deployment_url**: Your GitHub Pages URL
- **environment**: Current environment (dev/prod)
- **game_config**: Applied game settings
- **config_file_path**: Path to generated config
- **github_pages_instructions**: Step-by-step deployment guide

## 🚀 Complete Deployment Workflow

1. **Configure with Terraform**:

   ```bash
   cd src/infrastructure/terraform
   terraform apply -var-file="environments/prod.tfvars" -auto-approve
   ```

2. **Review Changes**:

   ```bash
   type ..\..\frontend\config.js
   ```

3. **Commit and Push**:

   ```bash
   git add ..\..\frontend\config.js
   git commit -m "Update game config via Terraform"
   git push origin main
   ```

4. **Enable GitHub Pages** (first time only):

   - Go to: https://github.com/mark-siazon/AE3-Terraform_Survivor/settings/pages
   - Set Source: Branch `main`, Folder `/src/frontend`
   - Click Save

5. **Play Your Game**:
   - Wait 1-2 minutes for GitHub Pages to deploy
   - Visit: https://mark-siazon.github.io/AE3-Terraform_Survivor/

## 🎓 Why Use Terraform?

This project demonstrates Infrastructure as Code (IaC) principles:

- **Version Control**: Game settings are tracked in Git
- **Reproducibility**: Same config every time
- **Environment Management**: Easy dev/staging/prod separation
- **Automation**: One command to update everything
- **Documentation**: Settings are self-documenting

## 🔄 Switching Environments

```bash
# Switch to easy mode
terraform apply -var-file="environments/dev.tfvars" -auto-approve

# Switch to hard mode
terraform apply -var-file="environments/prod.tfvars" -auto-approve

# View what would change (without applying)
terraform plan -var-file="environments/prod.tfvars"
```

## 📝 Notes

- GitHub Pages updates automatically when you push
- Changes take 1-2 minutes to go live
- Terraform only generates the config file
- GitHub Pages hosting is configured manually (one-time setup)
- The `.terraform` directory and `*.tfstate` files are gitignored

## 🐛 Troubleshooting

### Config not updating on GitHub Pages?

- Clear browser cache
- Wait 2-3 minutes for GitHub Pages to rebuild
- Check that you pushed the changes: `git log --oneline -1`

### Terraform errors?

```bash
# Reinitialize
terraform init

# Check syntax
terraform validate

# See what would change
terraform plan -var-file="environments/prod.tfvars"
```

### Want to see Terraform state?

```bash
terraform show
```

## 🎉 Success!

Your game is now deployed with Terraform-managed configuration! Every time you run `terraform apply`, you're using Infrastructure as Code to control your game's difficulty.
