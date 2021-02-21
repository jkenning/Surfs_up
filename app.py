# import dependencies
import datetime as dt 
import numpy as np 
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
# set up the database
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)
# save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# create session link from python to db
session = Session(engine)
# set up flask
app = Flask(__name__)
# define welcome route
@app.route("/")
# welcome return statement
def welcome():
    return(
        '''
        Welcome to the Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        ''')

