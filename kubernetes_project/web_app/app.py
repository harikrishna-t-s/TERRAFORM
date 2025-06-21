#!/usr/bin/env python3
"""
Simple Web Application for Kubernetes Learning
==============================================

This is a basic Flask web application designed for learning Docker and Kubernetes.
It includes basic functionality like health checks, environment variable support,
and simple web pages to demonstrate container orchestration concepts.

Author: Learning Project
Version: 1.0.0
"""

import os
import json
import platform
import socket
from datetime import datetime
from flask import Flask, render_template, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['APP_NAME'] = os.environ.get('APP_NAME', 'Kubernetes Learning App')
app.config['APP_VERSION'] = os.environ.get('APP_VERSION', '1.0.0')
app.config['ENVIRONMENT'] = os.environ.get('ENVIRONMENT', 'development')

def get_system_info():
    """Get system information for debugging and monitoring."""
    return {
        'hostname': socket.gethostname(),
        'platform': platform.platform(),
        'python_version': platform.python_version(),
        'environment': app.config['ENVIRONMENT'],
        'timestamp': datetime.now().isoformat()
    }

@app.route('/')
def index():
    """Main page of the application."""
    return render_template('index.html', 
                         app_name=app.config['APP_NAME'],
                         version=app.config['APP_VERSION'],
                         environment=app.config['ENVIRONMENT'])

@app.route('/health')
def health():
    """Health check endpoint for Kubernetes liveness and readiness probes."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'app_name': app.config['APP_NAME'],
        'version': app.config['APP_VERSION'],
        'environment': app.config['ENVIRONMENT']
    })

@app.route('/api/info')
def api_info():
    """API endpoint that returns application and system information."""
    return jsonify({
        'application': {
            'name': app.config['APP_NAME'],
            'version': app.config['APP_VERSION'],
            'environment': app.config['ENVIRONMENT']
        },
        'system': get_system_info(),
        'request': {
            'method': request.method,
            'url': request.url,
            'headers': dict(request.headers),
            'remote_addr': request.remote_addr
        }
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    """Echo endpoint that returns the sent data - useful for testing."""
    data = request.get_json() if request.is_json else request.form.to_dict()
    return jsonify({
        'message': 'Echo response',
        'received_data': data,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/status')
def status():
    """Status page showing application and system status."""
    return render_template('status.html',
                         app_name=app.config['APP_NAME'],
                         version=app.config['APP_VERSION'],
                         environment=app.config['ENVIRONMENT'],
                         system_info=get_system_info())

@app.errorhandler(404)
def not_found(error):
    """Custom 404 error handler."""
    return jsonify({
        'error': 'Not Found',
        'message': 'The requested resource was not found',
        'timestamp': datetime.now().isoformat()
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom 500 error handler."""
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An internal server error occurred',
        'timestamp': datetime.now().isoformat()
    }), 500

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Get host from environment variable or default to 0.0.0.0 for Docker
    host = os.environ.get('HOST', '0.0.0.0')
    
    # Debug mode based on environment
    debug = app.config['ENVIRONMENT'] == 'development'
    
    print(f"Starting {app.config['APP_NAME']} v{app.config['APP_VERSION']}")
    print(f"Environment: {app.config['ENVIRONMENT']}")
    print(f"Running on http://{host}:{port}")
    print(f"Debug mode: {debug}")
    
    app.run(host=host, port=port, debug=debug) 