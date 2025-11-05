# app/models/deck.py

from app import db
from datetime import datetime

class Deck(db.Model):
    """Deck model: a collection of cards under a user."""

    __tablename__ = "decks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    tags = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign Key to User
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Relationship: one deck can have many cards
    cards = db.relationship("Card", backref="deck", lazy=True, cascade="all, delete")

    def __repr__(self):
        return f"<Deck {self.title}>"
