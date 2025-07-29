from app import create_app
from app.extensions import db
from flask_migrate import Migrate, upgrade
from app.models import *  # Ensures Flask-Migrate sees all models

app = create_app()
migrate = Migrate(app, db)

# ✅ Auto-run migrations on server start (e.g., Render)
@app.before_first_request
def apply_migrations():
    try:
        upgrade()
        print("✅ Database migrations applied.")
    except Exception as e:
        print(f"❌ Migration error: {e}")
