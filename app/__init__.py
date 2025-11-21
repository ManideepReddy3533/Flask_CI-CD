from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.route1 import route1
    from app.routes.route2 import route2

    app.register_blueprint(route1)
    app.register_blueprint(route2)

    return app
