from flask import Flask, render_template
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 8080))

@app.route('/')
def index():
    data = {
        'title': 'sample data',
        'content': 'This is some placeholder content for the sample data.'
    }
    return data
    # return render_template('index.html')
    # return "Hello World"
@app.route('/second_page')
def second_page():
    # Placeholder data
    data = {
        'title': 'Second Page',
        'content': 'This is some placeholder content for the second page.'
    }
    return render_template('second_page.html', data=data)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=port)
