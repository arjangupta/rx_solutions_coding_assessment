from app import app
from flask import request

# This end-point expects a request with
# data type JSON that has only two keys, 
# user_latitude and user_longitude.
@app.route('/api', methods=['POST'])
def sole_api_endpoint():
    if request.is_json:
        json_dict = request.json
        if 'user_latitude' in json_dict and 'user_longitude' in json_dict:
            return 'Nearest pharmacy is unknown'
        else:
            return 'Error: request does not contain user\'s latitude and longitude', 400
    else:
        return 'Error: request is not JSON', 400