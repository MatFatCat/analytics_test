from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'JHKBJD,N7hbjnKLJDFNn,+_098y5uh'

    from website.views import views
    app.register_blueprint(views, url_prefix='/')

    return app

