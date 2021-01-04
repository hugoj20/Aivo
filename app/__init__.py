from flask import Flask, jsonify, current_app
from flask_restful import Api
from marshmallow import ValidationError
from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.db import db
from app.comfort.api.resources import comfort_v1
from .ext import ma, migrate

def create_app(settings_module):
    app = Flask(__name__)

    app.config.from_object(settings_module)

    db.init_app(app)
    ma.init_app(app)

    migrate.init_app(app, db)

    Api(app, catch_all_404s=True)

    app.url_map.strict_slashes = False
    
    app.register_blueprint(comfort_v1)

    register_error_handlers(app)

    return app

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        current_app.logger.info(str(e))
        return jsonify({'msg': 'Internal server error'}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404

    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return jsonify({'msg': str(e)}), 400