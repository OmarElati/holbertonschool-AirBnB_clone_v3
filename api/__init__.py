#!/usr/bin/python3
"""
Flask app module.
"""
from flask import Flask
import os
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_db(exception):
    """Close database or file storage"""
    storage.close()

if __name__ == "__main__":
    app.run(
        host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
        port=int(os.getenv('HBNB_API_PORT', '5000')),
        threaded=True,
        debug=True
    )
