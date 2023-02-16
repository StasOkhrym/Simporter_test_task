import os

from dotenv import load_dotenv
from flask import Flask

from api.api import api
from config import DevelopmentConfig, ProductionConfig

load_dotenv()


app = Flask(__name__)

if os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

app.register_blueprint(api, url_prefix="/api")


if __name__ == "__main__":
    app.run()
