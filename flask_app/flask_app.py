from flask import Flask
import sys
import matplotlib.pyplot as plt
import os
import numpy as np
import requests

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# get the location of ISS
def get_location():

    space_station_longitude = None
    space_station_latitude = None
    try:
        r = requests.get(url='http://api.open-notify.org/iss-now.json')
        location = r.json()

        space_station_longitude = float(location['iss_position']['longitude'])
        space_station_latitude = float(location['iss_position']['latitude'])

    except:
        print('Request not working')
    return (space_station_longitude, space_station_latitude)

def translate_to_pixels(longitude, latitude, max_x_px, max_y_px):
    # y = -90 to 90 and x = -180 to 180
    scale_x = abs(((longitude + 180) / 360) * max_x_px)
    scale_y = abs(((latitude - 90) / 180) * max_y_px) #y scale is flipped

    return scale_x, scale_y