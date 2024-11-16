from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize db and migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Initialize db and migrate with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import routes inside the function to avoid circular import
    from . import routes
    app.register_blueprint(routes.main)

    with app.app_context():
        db.create_all()

    return app
