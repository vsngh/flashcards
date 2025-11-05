# run.py

from app import create_app, db
from app.models import User, Deck, Card

# Create the Flask app instance using the factory function
app = create_app("development")

# Optional: allows Flask shell to access your models directly
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Deck": Deck, "Card": Card}

# This ensures the app only runs when executed directly, not on import
if __name__ == "__main__":
    app.run(debug=True)
