import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np
import pandas as pd
import datetime as dt
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)


@app.route("/")
def welcome():

    return( """
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    """)


@app.route("/api/v1.0/precipitation")

def precipitation ():
    return


@app.route("/api/v1.0/stations")

def stations ():
    return


@app.route("/api/v1.0/tobs")

def stats():
    return

@app.route("/api/v1.0/temp/start/end")

def monthly_temps ():
    