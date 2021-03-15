""" Script to get oauth access token from strava

This is just a temporary solution!
"""

from secrets import *
from stravaio import strava_oauth2      # just for authentication to get token
from stravaio import StravaIO
import requests

auth = strava_oauth2(client_id=STRAVA_CLIENT_ID,
    client_secret=STRAVA_CLIENT_SECRET)
print('Access Token = ' +  auth['access_token'])
print('Refresh Token = ' +  auth['refresh_token'])


