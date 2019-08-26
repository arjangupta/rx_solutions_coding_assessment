from app import app
from flask import request

# This end-point expects a request with
# data type JSON that has only two keys, 
# latitude and longitude.
@app.route('/api', methods=['POST'])
def sole_api_endpoint():
    if request.is_json:
        json_message = request.json
        return 'Nearest pharmacy is unknown'
    else:
        return 'Error: request is not JSON'