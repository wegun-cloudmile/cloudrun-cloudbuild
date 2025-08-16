from flask import Flask, render_template
import os
app = Flask(__name__)

# Define a route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for page_two
@app.route('/page_two')
def page_two():
    return render_template('page_two.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)