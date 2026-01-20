# Copilot Instructions for Automation Inventory Management

## Project Overview
- This is a Django-based inventory management system.
- Major apps: `inventory` (core inventory logic), `apiapp` (API endpoints).
- Data is stored in `db.sqlite3` and managed via Django ORM models in each app's `models.py`.
- Templates are in `templates/` (global) and `apiapp/templates/` (app-specific).
- Static assets are in `static/` (CSS, JS, fonts, images).

## Key Workflows
- **Run server:** `python manage.py runserver` (from project root)
- **Migrations:**
  - Create: `python manage.py makemigrations <app>`
  - Apply: `python manage.py migrate`
- **Create superuser:** `python manage.py createsuperuser`
- **Tests:** `python manage.py test <app>`
- **Build (PyInstaller):** See `inventory.spec` for build config; output in `build/`.

## Project Structure & Conventions
- Each Django app has its own `models.py`, `views.py`, `urls.py`, `admin.py`, and `migrations/`.
- Main project config: `AUtomation_inventory_management/settings.py` and `urls.py`.
- Use Django's class-based views and forms where possible (see `inventory/forms.py`).
- API endpoints are defined in `apiapp/urls.py` and `apiapp/views.py`.
- Templates use Django templating; static files referenced via `{% static %}`.
- Custom logic for inventory, history, and product management is in `inventory/`.
- Use `myenv/` for the Python virtual environment (activate before running commands).

## Integration & Patterns
- Cross-app communication via Django signals or direct model imports.
- No external API integrations detected (as of this analysis).
- PyInstaller is used for packaging; see `inventory.spec` for details.

## Examples
- To add a new model: Edit `models.py` in the relevant app, run makemigrations/migrate.
- To add a new page: Add a template, update `urls.py` and `views.py` in the relevant app.
- To add a static asset: Place in `static/` and reference in templates.

## References
- Main Django config: `AUtomation_inventory_management/settings.py`
- Inventory logic: `inventory/`
- API endpoints: `apiapp/`
- Templates: `templates/`, `apiapp/templates/`
- Static files: `static/`

---

_If you update project structure or workflows, please update this file to keep AI agents productive._
