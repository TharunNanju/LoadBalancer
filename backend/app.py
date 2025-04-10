from flask import Flask
import socket
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests', ['container'])

@app.route('/')
def home():
    REQUEST_COUNT.labels(container=socket.gethostname()).inc()
    return f"Hello from container: {socket.gethostname()}"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000, debug=True)
=======
    app.run(host='0.0.0.0', port=5000)

>>>>>>> parent of 6af89ff (Post Presentation code)
