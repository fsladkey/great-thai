import os
from db_interface.query_helpers import all_cuisines, top_ten_by_grade, grade_distribution
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/api/cuisines')
def cuisines():
    data = all_cuisines()
    return jsonify(data)


@app.route('/api/cuisines/stats/')
def cuisine_stats():
    cuisine = request.args.get('cuisine')
    data = {
      "top_ten": top_ten_by_grade(cuisine),
      "grade_distribution": grade_distribution(cuisine)
    }
    return jsonify(data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
