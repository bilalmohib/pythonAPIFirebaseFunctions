import time
from flask import Flask, render_template
import os
from api import create_app  # Import the create_api function

# Call create_api function to create the Flask app instance
app = create_app()

def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)

@app.route('/')
def index():
    context = {
        'server_time': format_server_time()
    }
    # return render_template('index.html', context=context)
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
