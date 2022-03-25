from flask import Flask


def create_app():
  app = Flask(__name__)

  app.config["SECRET_KEY"] = 'd8fd8afae87fe7686159fb2e78bc6e25d6495d3852f74f03beafb15385c2c484'
  from .views import views

  app.register_blueprint(views, url_prefix='/')
  
  return app
