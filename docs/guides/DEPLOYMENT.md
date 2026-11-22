# 🚀 Deployment Guide

Complete guide for deploying Terraform Survivor to free hosting platforms.

## Quick Deploy Options

| Platform               | Cost | Setup Time | Best For                        |
| ---------------------- | ---- | ---------- | ------------------------------- |
| **GitHub Pages**       | Free | 2 min      | Simplest, no config needed      |
| **Vercel**             | Free | 5 min      | Auto-deploy, preview URLs       |
| **Vercel + Terraform** | Free | 10 min     | Full IaC, multiple environments |

---

## 🎯 Option 1: GitHub Pages (Easiest)

**Perfect for**: Quick deployment, no configuration needed

### Step 1: Push to GitHub

```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/terraform-survivor.git
git branch -M main
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Go to your repo on GitHub
2. Click **Settings** → **Pages**
3. Under **Source**, select:
   - Branch: `main`
   - Folder: `/src/frontend`
4. Click **Save**

### Step 3: Access Your Game

Your game will be live at:

```
https://YOUR_USERNAME.github.io/terraform-survivor/
```

### Update Game Config

To change difficulty with Terraform:

```bash
# Generate new config
cd src/infrastructure/terraform
terraform init
terraform apply -var-file="environments/prod.tfvars"

# Commit and push
git add ../../frontend/config.js
git commit -m "Update to hard mode"
git push
```

GitHub Pages will auto-deploy in ~1 minute!

---

## 🚀 Option 2: Vercel (Recommended)

**Perfect for**: Auto-deploy, preview URLs, custom domains

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

### Step 2: Deploy

```bash
# From project root
cd src/frontend
vercel

# Follow prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name? terraform-survivor
# - Directory? ./ (current)
# - Override settings? No
```

### Step 3: Production Deploy

```bash
vercel --prod
```

Your game is now live! Vercel will give you a URL like:

```
https://terraform-survivor.vercel.app
```

### Auto-Deploy from GitHub

```bash
# Link to GitHub repo
vercel git connect

# Now every push auto-deploys!
git push origin main
```

### Update Config with Terraform

```bash
cd ../../infrastructure/terraform
terraform apply -var-file="environments/prod.tfvars"

# Deploy updated config
cd ../../frontend
vercel --prod
```

---

## 🏗️ Option 3: Vercel + Terraform (Full IaC)

**Perfect for**: Multiple environments, full automation, team projects

### Prerequisites

1. **Vercel Account** - Sign up at [vercel.com](https://vercel.com)
2. **Vercel API Token**:
   - Go to [vercel.com/account/tokens](https://vercel.com/account/tokens)
   - Click **Create**
   - Name it "Terraform"
   - Copy the token

### Step 1: Set API Token

```bash
# Windows (CMD)
set VERCEL_API_TOKEN=your_token_here

# Windows (PowerShell)
$env:VERCEL_API_TOKEN="your_token_here"

# Mac/Linux
export VERCEL_API_TOKEN=your_token_here
```

### Step 2: Update Terraform Config

Edit `src/infrastructure/terraform/main.tf`:

```hcl
# Uncomment and update:
variable "github_repo" {
  default = "YOUR_USERNAME/terraform-survivor"
}
```

### Step 3: Deploy with Terraform

```bash
cd src/infrastructure/terraform

# Initialize
terraform init

# Deploy to development
terraform apply -var-file="environments/dev.tfvars"

# Deploy to production
terraform apply -var-file="environments/prod.tfvars"
```

### Step 4: Get Your URLs

```bash
terraform output deployment_url
```

### Multiple Environments

Deploy different difficulty levels to different URLs:

```bash
# Easy mode (dev)
terraform apply -var-file="environments/dev.tfvars"
# → https://terraform-survivor-dev.vercel.app

# Normal mode (staging)
terraform apply -var-file="environments/staging.tfvars"
# → https://terraform-survivor-staging.vercel.app

# Hard mode (prod)
terraform apply -var-file="environments/prod.tfvars"
# → https://terraform-survivor-prod.vercel.app
```

---

## 🔄 Hybrid: GitHub + Vercel

**Perfect for**: Best of both worlds

### Setup

1. **Push to GitHub** (see Option 1)
2. **Connect Vercel to GitHub**:
   - Go to [vercel.com/new](https://vercel.com/new)
   - Import your GitHub repo
   - Set **Root Directory**: `src/frontend`
   - Click **Deploy**

### Benefits

- ✅ Auto-deploy on every push
- ✅ Preview URLs for pull requests
- ✅ Easy rollbacks
- ✅ Custom domains
- ✅ Analytics

### Update Workflow

```bash
# 1. Update config with Terraform
cd src/infrastructure/terraform
terraform apply -var-file="environments/prod.tfvars"

# 2. Commit and push
git add ../../frontend/config.js
git commit -m "Update difficulty to hard mode"
git push

# 3. Vercel auto-deploys!
```

---

## 🎮 Custom Domain

### GitHub Pages

1. Go to **Settings** → **Pages**
2. Enter your domain under **Custom domain**
3. Add DNS records:
   ```
   Type: CNAME
   Name: www
   Value: YOUR_USERNAME.github.io
   ```

### Vercel

```bash
# Add domain
vercel domains add yourdomain.com

# Follow DNS instructions
```

Or in Vercel dashboard:

1. Go to your project
2. **Settings** → **Domains**
3. Add your domain
4. Update DNS records

---

## 🔧 Environment Variables

### Vercel Dashboard

1. Go to project **Settings** → **Environment Variables**
2. Add variables:
   ```
   GAME_ENVIRONMENT=production
   GAME_DIFFICULTY=hard
   ```

### Terraform

Already configured in `main.tf`:

```hcl
environment = [
  {
    key    = "GAME_ENVIRONMENT"
    value  = var.environment
    target = ["production", "preview"]
  }
]
```

---

## 📊 Comparison

| Feature           | GitHub Pages | Vercel | Vercel + Terraform |
| ----------------- | ------------ | ------ | ------------------ |
| **Cost**          | Free         | Free   | Free               |
| **Setup Time**    | 2 min        | 5 min  | 10 min             |
| **Auto-deploy**   | ✅           | ✅     | ✅                 |
| **Preview URLs**  | ❌           | ✅     | ✅                 |
| **Custom Domain** | ✅           | ✅     | ✅                 |
| **Multiple Envs** | ❌           | Manual | ✅ Automated       |
| **Analytics**     | ❌           | ✅     | ✅                 |
| **Rollbacks**     | Manual       | ✅     | ✅                 |
| **IaC**           | ❌           | ❌     | ✅                 |

---

## 🐛 Troubleshooting

### GitHub Pages 404

**Problem**: Page shows 404  
**Solution**:

- Check **Settings** → **Pages** → Source is `/src/frontend`
- Wait 1-2 minutes for deployment
- Clear browser cache

### Vercel Build Fails

**Problem**: Deployment fails  
**Solution**:

```bash
# Check build locally
cd src/frontend
python -m http.server 8000 --bind 127.0.0.1
# If it works locally, it should work on Vercel
```

### Terraform Can't Connect to Vercel

**Problem**: `Error: authentication failed`  
**Solution**:

```bash
# Verify token is set
echo $VERCEL_API_TOKEN  # Mac/Linux
echo %VERCEL_API_TOKEN%  # Windows CMD
echo $env:VERCEL_API_TOKEN  # Windows PowerShell

# If empty, set it again
export VERCEL_API_TOKEN=your_token_here
```

### Config Not Updating

**Problem**: Game difficulty doesn't change  
**Solution**:

```bash
# Regenerate config
cd src/infrastructure/terraform
terraform apply -var-file="environments/prod.tfvars"

# Verify config was generated
cat ../../frontend/config.js

# Redeploy
git add ../../frontend/config.js
git commit -m "Update config"
git push
```

---

## 🎯 Recommended Workflow

### For Personal Projects

→ **GitHub Pages** (simplest)

### For Portfolio/Demo

→ **Vercel** (looks professional)

### For Learning Terraform

→ **Vercel + Terraform** (full IaC experience)

### For Team Projects

→ **GitHub + Vercel** (best collaboration)

---

## 📝 Quick Commands Reference

```bash
# GitHub Pages
git push origin main

# Vercel
vercel --prod

# Terraform
cd src/infrastructure/terraform
terraform apply -var-file="environments/prod.tfvars"

# Update config and deploy
terraform apply -var-file="environments/prod.tfvars"
git add ../../frontend/config.js
git commit -m "Update config"
git push  # or: vercel --prod
```

---

## 🎉 Success!

Your game is now deployed! Share your URL:

- GitHub Pages: `https://YOUR_USERNAME.github.io/terraform-survivor/`
- Vercel: `https://terraform-survivor.vercel.app`

**Next steps:**

- Add custom domain
- Set up multiple environments
- Share with friends!
