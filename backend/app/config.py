# app/config.py

import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "superjwtkey")


class DevelopmentConfig(Config):
    """Development config using local SQLite database."""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///grok.db")
    DEBUG = True


class ProductionConfig(Config):
    """Production config with real database (e.g., PostgreSQL)."""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    DEBUG = False
