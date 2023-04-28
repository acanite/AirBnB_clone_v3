#!/usr/bin/python3
"""
index - Create an endpoint that retrieves the
number of each objects by type:
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """ returns a JSON: "status": "OK" """
    return jsonify(status="OK")


@app_views.route('/api/v1/stats')
def stats():
    """ Create an endpoint that retrieves
    the number of each objects by type:
    """
    return jsonify(amenities=storage.count("Amenities"),
                   cities=storage.count("Cities"),
                   places=storage.count("Places"),
                   reviews=storage.count("Reviews"),
                   states=storage.count("States"),
                   users=storage.count("Users")
                   )
