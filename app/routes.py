from app import app
from flask import request

@app.route('/api', methods=['POST'])
def sole_api_endpoint():
    message = request.json
    print(message)
    return message