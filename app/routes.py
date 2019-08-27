from app import app
from app.models import Pharmacy
from flask import request
import geopy.distance

# Get list of pharmacies 
pharmacies_by_latitude = Pharmacy.query.order_by(Pharmacy.latitude).all()

# Utility function
def find_closest_pharmacy(user_latitude, user_longitude):
    user_coordinate = (user_latitude, user_longitude)
    for p in pharmacies_by_latitude:
        pharmacy_coordinate = (p.latitude, p.longitude)
        displacement = geopy.distance.distance(user_coordinate, pharmacy_coordinate).miles
    return 0

# This end-point expects a request with
# data type JSON that has only two keys, 
# user_latitude and user_longitude.
@app.route('/api', methods=['POST'])
def sole_api_endpoint():
    global pharmacies_by_latitude
    if request.is_json:
        json_dict = request.json
        if 'user_latitude' in json_dict and 'user_longitude' in json_dict:
            closest_pharmacy = find_closest_pharmacy(json_dict.get('user_latitude'), json_dict.get('user_longitude'))
            return 'Nearest pharmacy is unknown'
        else:
            return 'Error: request does not contain user\'s latitude and longitude', 400
    else:
        return 'Error: request is not JSON', 400