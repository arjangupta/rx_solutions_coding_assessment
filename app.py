from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api_endpoint():
    json = '{}'
    return json

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    print('Started server, begin serving forever')
    http_server.serve_forever()