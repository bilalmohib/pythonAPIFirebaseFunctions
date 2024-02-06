from flask import Flask, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
port = int(os.environ.get("PORT", 8080))

@app.route('/')
def index():
    return render_template('index.html')
    # return "Hello World"
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=port)