from flask import Flask
import os


def create_app(test_config=None):
    from .db import init_app
    from .routes.auth import bp as auth_bp
    from .routes.index import bp as index_bp
    from .routes.upload import bp as upload_bp

    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "app.sqlite")
    )

    init_app(app)

    if test_config is None:
        app.config.from_pyfile(
            "config.py",
        )
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(upload_bp)

    return app
