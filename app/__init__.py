from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config.settings import Config


# Inisialisasi ekstensi
db = SQLAlchemy()
migrate = Migrate()


def create_app():

    app = Flask(__name__)

    # Memuat konfigurasi
    app.config.from_object(Config)

    # Menghubungkan ekstensi dengan Flask
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return {
            "success": True,
            "message": "Flask User API is running"
        }, 200

    return app