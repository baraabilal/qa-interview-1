"""
To run the app, do the following.

$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/

"""
import sys

from flask import Flask, jsonify, render_template, request

import logging

sys.path.append('.')
from helpers.score import calculate_score
from helpers.io import load_data, write_response, load_responses

app = Flask(__name__)
app.debug = True
logger = logging.getLogger('__main__')
logging.basicConfig(filename='error.log', level=logging.DEBUG)
logger.info('Logging configured')


@app.route("/questions", methods=['GET', 'POST'])
def get_data():
    "Endpoint for getting questions and submitting respones"
    rows = load_data()

    if request.method == 'GET':
        return jsonify({'questions': [r[1] for r in rows]}), 200

    if request.method == 'POST':
        return jsonify({'answers': [(r[2]) for r in rows]}), 200


@app.route("/submit/<id>/<response>", methods=['POST'])
def submit_responses(id, response):
    r = {'id': id, 'response': response}
    _ = str(write_response(r))
    return 'Submitted {}'.format(r), 200


@app.route("/get_score")
def get_score():
    "Calculate a score from submitted responses"
    data = load_data()
    correct_answers = [r[2] for r in data]
    responses = load_responses()
    score = calculate_score(responses, correct_answers)
    return jsonify({'score': score}), 200
    