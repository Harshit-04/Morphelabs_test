from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getlogin()

    # Get server time in IST
    tz = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

    # Get top command output
    top_output = subprocess.getoutput('top -b -n 1')

    # Create HTML content
    html = f"""
    <html>
    <head><title>/htop Endpoint</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> Harshit Tuli</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Command Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
