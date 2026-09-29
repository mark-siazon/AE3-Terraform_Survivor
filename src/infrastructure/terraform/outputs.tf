output "deployment_url" {
  description = "URL of the deployed game on GitHub Pages"
  value       = "https://mark-siazon.github.io/AE3-Terraform_Survivor/"
}

output "environment" {
  description = "Deployed environment"
  value       = var.environment
}

output "game_config" {
  description = "Current game configuration"
  value = {
    difficulty          = var.difficulty
    hunger_decay        = var.game_settings.hunger_decay_rate
    thirst_decay        = var.game_settings.thirst_decay_rate
    danger_level        = var.game_settings.danger_level
    resource_multiplier = var.game_settings.resource_multiplier
    crafting_enabled    = var.features.crafting_enabled
  }
}
