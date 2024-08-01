# Archivo: presentacion/__init__.py
from flask import Flask
from presentacion.controladores.participantes_controller import participantes_bp
from presentacion.controladores.proceso_electoral_controller import proceso_electoral_bp


def create_app():
    """
    Crea y configura una instancia de la aplicación Flask.
    
    Returns:
        app (Flask): La instancia de la aplicación Flask configurada.
    """
    app = Flask(__name__)

    # Registro de Blueprints
    app.register_blueprint(participantes_bp)
    app.register_blueprint(proceso_electoral_bp)

    return app
