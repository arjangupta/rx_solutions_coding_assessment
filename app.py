from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api_endpoint():
    json = '{}'
    return json

if __name__ == '__main__':
    print('Server is up and running')
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()