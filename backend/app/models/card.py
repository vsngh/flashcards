# app/models/card.py

from app import db
from datetime import datetime, timedelta

class Card(db.Model):
    """Card model: represents a single flashcard in a deck."""

    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.Text, nullable=False)
    back = db.Column(db.Text, nullable=False)
    progress = db.Column(db.Integer, default=0)  # How well user remembers this card
    next_study_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key to Deck
    deck_id = db.Column(db.Integer, db.ForeignKey("decks.id"), nullable=False)

    def update_progress(self, correct: bool):
        """
        Updates progress and next study date based on whether the answer was correct.
        This is a simple spaced repetition logic.
        """
        if correct:
            self.progress += 1
            self.next_study_date = datetime.utcnow() + timedelta(days=self.progress)
        else:
            self.progress = max(0, self.progress - 1)
            self.next_study_date = datetime.utcnow() + timedelta(days=1)

    def __repr__(self):
        return f"<Card {self.front[:20]}...>"
