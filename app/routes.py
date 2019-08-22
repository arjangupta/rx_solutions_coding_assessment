from app import app
from flask import request

@app.route('/api', methods=['POST'])
def sole_api_endpoint():
    if request.is_json:
        message = request.json
        # print(message)
        return message
    else:
        return 'Error: request is not JSON'