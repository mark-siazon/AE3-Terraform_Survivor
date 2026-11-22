# ⚡ Quick Reference Card

## 🎮 Controls

| Key     | Action   | Energy | Description                     |
| ------- | -------- | ------ | ------------------------------- |
| **E**   | Explore  | 15     | Find wood, stone, or berries    |
| **H**   | Hunt     | 20     | Hunt for meat (risky)           |
| **W**   | Water    | 10     | Gather water, restore thirst    |
| **F**   | Eat Food | 0      | Consume berries or meat         |
| **R**   | Rest     | 0      | Sleep, recover energy, next day |
| **C**   | Craft    | 5      | Build items from resources      |
| **S**   | Status   | 0      | View detailed stats             |
| **O**   | Settings | 0      | Adjust difficulty               |
| **?**   | Help     | 0      | Show shortcuts                  |
| **ESC** | Close    | 0      | Close any dialog                |

## 📊 Stats

- **Health** 💚 - Don't let it reach 0!
- **Hunger** 🍖 - Eat berries or meat
- **Thirst** 💧 - Gather water regularly
- **Energy** ⚡ - Rest to recover

## 🎯 Survival Tips

1. **Click low stats** - Get instant help and solutions!
2. **Click food in inventory** - Fastest way to eat
3. **Keep stats above 50%** - Safer buffer
4. **Watch for pulsing stats** - They need attention
5. **Green tooltips** - Click to fix instantly
6. **Orange tooltips** - Gather items first
7. **Rest when energy is low** - Can't act without energy
8. **Hunt carefully** - High risk, high reward
9. **Explore often** - Gather resources early
10. **Adjust settings** - Too hard? Lower the difficulty!

## 🏆 Achievements

| Icon | Name      | Requirement           |
| ---- | --------- | --------------------- |
| 🏕️   | Survivor  | Survive 10 days       |
| ⛺   | Veteran   | Survive 25 days       |
| 🏔️   | Legend    | Survive 50 days       |
| 👑   | Immortal  | Survive 100 days      |
| 🔍   | Explorer  | Explore 50 times      |
| 🏹   | Hunter    | Hunt 25 times         |
| 🔨   | Craftsman | Craft 10 items        |
| 📦   | Gatherer  | Collect 100 resources |
| 🏛️   | Hoarder   | Collect 500 resources |

## ⚙️ Settings

Adjust in real-time (press **O**):

- **Hunger Decay** (1-10) - How fast you get hungry
- **Thirst Decay** (1-10) - How fast you get thirsty
- **Energy Decay** (1-10) - How fast you tire
- **Danger Level** (0-100%) - Event probability
- **Resources** (0.5x-3x) - Resource multiplier

## 🔨 Crafting

| Item        | Materials        | Effect                 |
| ----------- | ---------------- | ---------------------- |
| 🔥 Campfire | 5 wood, 3 stone  | Cook food efficiently  |
| 🏠 Shelter  | 10 wood, 5 stone | Better rest recovery   |
| 🗡️ Spear    | 3 wood, 2 stone  | Better hunting success |

## 💾 Save System

- **Auto-save**: Every 30 seconds
- **Manual save**: Click Save button
- **Auto-load**: Loads on startup
- **Storage**: Browser localStorage

## 🚀 Quick Start

```bash
# Play locally
python run-game.py
# Open: http://127.0.0.1:8000/standalone.html

# Or use standalone
# Just open: src/frontend/standalone.html

# Deploy to GitHub Pages
git push origin main
# Enable Pages in repo settings

# Use Terraform for difficulty
cd src/infrastructure/terraform
terraform apply -var-file="environments/dev.tfvars"
```

## 🎲 Terraform Presets

```bash
# Easy Mode (Development)
terraform apply -var-file="environments/dev.tfvars"
# 2x resources, 10% danger, lots of starting items

# Normal Mode (Staging)
terraform apply -var-file="environments/staging.tfvars"
# Balanced, 30% danger, standard resources

# Hard Mode (Production)
terraform apply -var-file="environments/prod.tfvars"
# 0.8x resources, 50% danger, minimal items
```

## 🐛 Troubleshooting

**Game won't load?**

- Use HTTP server (not file://)
- Check browser console (F12)
- Verify config.js exists

**Save not working?**

- Enable localStorage in browser
- Check privacy settings
- Try non-incognito mode

**Config not updating?**

- Run `terraform apply` again
- Hard refresh (Ctrl+F5)
- Check config.js was generated

**Stats not showing?**

- Play at least one game
- Check localStorage enabled
- View in Statistics panel

## 📱 Browser Support

✅ Chrome 90+
✅ Firefox 88+
✅ Safari 14+
✅ Edge 90+

## 🔗 Links

- [Full Documentation](README.md)
- [Feature List](FEATURES.md)
- [Developer Guide](DEVELOPER_GUIDE.md)
- [Changelog](CHANGELOG.md)

---

**Print this card for quick reference while playing!**
