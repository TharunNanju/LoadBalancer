from flask import Flask, render_template
import socket
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)  # No need to specify template_folder if it's ./templates

REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests', ['container'])

@app.route('/')
def home():
    container_name = socket.gethostname()
    REQUEST_COUNT.labels(container=container_name).inc()
    return render_template('index.html', container_name=container_name)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
