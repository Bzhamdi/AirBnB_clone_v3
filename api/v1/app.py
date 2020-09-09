#!/usr/bin/python3
"""task 8"""
import models
from api.v1.views import app_views
from flask import Flask
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardo_db(session):
    """close session"""
    models.storage.close()


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=os.getenv('HBNB_API_PORT', '5000'))
