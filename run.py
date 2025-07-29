from app import create_app
from app.extensions import db
from flask_migrate import Migrate, upgrade
from app.models import *  # Ensures Flask-Migrate sees all models

app = create_app()
migrate = Migrate(app, db)

# ✅ Auto-run migrations when deployed (e.g., on Render)
if __name__ == "__main__":
    import os
    if os.environ.get("RENDER"):  # Only run this on Render deployment
        with app.app_context():
            try:
                upgrade()
                print("✅ Database migrations applied.")
            except Exception as e:
                print(f"❌ Migration error: {e}")

    app.run()
