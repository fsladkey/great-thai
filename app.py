import os
from query_helpers import all_restaurants
from flask import Flask, render_template, jsonify, url_for
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')

@app.route('/api/data')
def data():
    data = all_restaurants()
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
