# AGENTS.md

## Scope
- Terraform Survivor cloud infrastructure learning game (`mark-siazon/AE3-Terraform_Survivor`, branch `main`).
- Follow root `C:\Codes Local\AGENTS.md` first, then this file.

## Project Layout
- `run-game.py` — Python entrypoint to serve/launch the game locally
- `start-game.bat` — Windows batch launcher
- `src/frontend/` — static web game files
- `src/infrastructure/terraform/` — Terraform IaC modules
- `.github/workflows/deploy-pages.yml` — GitHub Pages deployment workflow

## Key Commands
- `python run-game.py` — launch the local game server

## Change Control & Verification
- Keep changes scoped to the target module and verify `python run-game.py` or static HTML/Terraform changes before finishing.
- Never commit Terraform state files or credentials.
