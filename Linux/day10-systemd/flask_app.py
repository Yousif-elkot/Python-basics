"""
FLASK APP PSEUDOCODE:
1. Import Flask
2. Create Flask application instance
3. Define a route for "/" that returns a welcome message
4. Define a route for "/health" that returns status
5. Run the server on host 0.0.0.0, port 5000
"""

from flask import Flask, jsonify
from datetime import datetime
import os
import signal
import sys

app = Flask(__name__)

# store startup time
START_TIME = datetime.now()

@app.route('/')
def home():
    """Main endpoint returning a welcome message."""
    return jsonify({
        'message': 'Flask App Managed by systemd',
        'status': 'running',
        'uptime': str(datetime.now() - START_TIME),
        'pid': os.getpid()
    })

@app.route('/health')
def health():
    """Health check endpoint - for monitoring."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200

def graceful_shutdown(signum, frame):
    """Handle graceful shutdown on receiving termination signals."""
    print(f"Received signal {signum}. Shutting down gracefully...")
    sys.exit(0)

if __name__ == '__main__':
    # Register signal handlers for graceful shutdown
    signal.signal(signal.SIGTERM, graceful_shutdown)
    signal.signal(signal.SIGINT, graceful_shutdown)

    # Run the Flask app
    # host='0.0.0.0' makes it accessible from outside localhost
    app.run(host='0.0.0.0', port=5000 , debug=False)

