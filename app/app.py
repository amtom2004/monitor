from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

VERSION = os.getenv('APP_VERSION', '3.0')
HOSTNAME = socket.gethostname()

@app.route('/')
def home():
    return jsonify({
        "message": f"Hello, from Monitor Version {VERSION}",
        "hostname": HOSTNAME,
        "version": VERSION 
    })

@app.route('/health/live')
def liveness():
    return jsonify({
        "status": "alive"
    })

@app.route('/health/ready')
def readiness():
    return jsonify({
        "status": "ready"
    })

@app.route('/version')
def version():
    return jsonify({
        "version": VERSION,
        "hostname": HOSTNAME
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


# argocd login localhost:8080 --insecure --username admin --password $(kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d)