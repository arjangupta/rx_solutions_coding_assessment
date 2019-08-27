from app import app
from app.models import Pharmacy
from flask import request

# Get list of pharmacies 
pharmacies_by_latitude = Pharmacy.query.order_by(Pharmacy.latitude).all()

# This end-point expects a request with
# data type JSON that has only two keys, 
# user_latitude and user_longitude.
@app.route('/api', methods=['POST'])
def sole_api_endpoint():
    global pharmacies_by_latitude
    if request.is_json:
        json_dict = request.json
        if 'user_latitude' in json_dict and 'user_longitude' in json_dict:
            user_latitude  = json_dict.get('user_latitude')
            user_longitude = json_dict.get('user_longitude')
            print(f'User latitude: {user_latitude}, and longitude: {user_longitude}')
            return 'Nearest pharmacy is unknown'
        else:
            return 'Error: request does not contain user\'s latitude and longitude', 400
    else:
        return 'Error: request is not JSON', 400