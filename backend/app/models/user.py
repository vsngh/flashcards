# app/models/user.py

from app import db, bcrypt
from datetime import datetime

class User(db.Model):
    """User model represents app users."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship: one user can have many decks
    decks = db.relationship("Deck", backref="author", lazy=True)

    def set_password(self, password):
        """Hashes a password before saving."""
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """Checks a given password against the stored hash."""
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"
