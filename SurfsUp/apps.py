import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Main Page
@app.route("/")
def main():
    """List of available routes"""
    return(
        f"Welcome to my Hawaiian Vacation Weather Page"
        f"Listed are the routes towards different weather analysis completed to help determine my vacation destination:"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"

    )

@app.route("/api/v1.0/precipitation")
@app.route("/api/v1.0/stations")
@app.route("/api/v1.0/tobs")