from flask import Flask, request
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api_endpoint():
    json = 'You successfully hit the endpoint'
    return json

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    print('Started server, begin serving forever')
    http_server.serve_forever()