# GitHub Pages deployment outputs
# The main configuration is in main.tf

output "github_pages_instructions" {
  value = <<-EOT
    
    ✅ Configuration generated successfully!
    
    Next steps for GitHub Pages deployment:
    
    1. Review the generated config:
       type ..\..\frontend\config.js
    
    2. Commit and push to GitHub:
       git add ..\..\frontend\config.js
       git commit -m "Update game config via Terraform (${var.difficulty} mode)"
       git push origin main
    
    3. Enable GitHub Pages (if not already enabled):
       - Go to: https://github.com/mark-siazon/AE3-Terraform_Survivor/settings/pages
       - Set Source: Branch 'main', Folder '/src/frontend'
       - Click Save
    
    4. Your game will be live at:
       https://mark-siazon.github.io/AE3-Terraform_Survivor/
    
    Game Settings Applied:
    - Environment: ${var.environment}
    - Difficulty: ${var.difficulty}
    - Hunger Decay: ${var.game_settings.hunger_decay_rate}
    - Resource Multiplier: ${var.game_settings.resource_multiplier}
    - Danger Level: ${var.game_settings.danger_level}
  EOT
  description = "Instructions for completing the GitHub Pages deployment"
}
