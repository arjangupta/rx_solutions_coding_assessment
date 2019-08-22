from app import app
from flask import request

# This end-point expects a request with
# data type JSON that has only two keys, 
# latitude and longitude.
@app.route('/api', methods=['POST'])
def sole_api_endpoint():
    if request.is_json:
        message = request.json
        return message
    else:
        return 'Error: request is not JSON'