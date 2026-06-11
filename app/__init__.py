from flask import Flask


def create_app():

    app = Flask(
        __name__
    )

    # ===============================
    # BASIC ROUTES
    # ===============================

    from app.routes.dashboard import (
        dashboard_bp
    )

    from app.routes.intelligent_systems import (
        intelligent_systems_bp
    )

    from app.routes.paradigms import (
        paradigms_bp
    )

    from app.routes.kdd import (
        kdd_bp
    )

    from app.routes.documentation import (
        documentation_bp
    )

    # ===============================
    # AI MODULES
    # ===============================

    from app.modules.predictive.routes import (
        predictive_bp
    )

    from app.modules.nlp.routes import (
        nlp_bp
    )

    from app.modules.vision.routes import (
        vision_bp
    )

    # ===============================
    # REGISTER BASIC ROUTES
    # ===============================

    app.register_blueprint(
        dashboard_bp
    )

    app.register_blueprint(
        intelligent_systems_bp
    )

    app.register_blueprint(
        paradigms_bp
    )

    app.register_blueprint(
        kdd_bp
    )

    app.register_blueprint(
        documentation_bp
    )

    # ===============================
    # REGISTER AI MODULES
    # ===============================

    app.register_blueprint(
        predictive_bp
    )

    app.register_blueprint(
        nlp_bp
    )

    app.register_blueprint(
        vision_bp
    )

    return app
