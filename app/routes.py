from app import app

@app.route('/api', methods=['POST'])
def sole_api_endpoint():
    message = 'You successfully hit the endpoint'
    return message