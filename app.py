## @app.py
# This file loads corresponding logic, and html template file(s), which
#     allows the presentation of (asynchronous) content.
import json
from flask import Flask, render_template, request
from logic.validation import validate_alphanum
from logic.parser import get_content
from logic.utility import linear_merge

# Initialize: create flask instance
app = Flask(__name__)

# index: define HTML template for base URL
@app.route('/')
def index():
    return render_template('index.html')

## quiz: main logic
@app.route('/quiz/merge', methods=['POST', 'GET'])
def quiz():

    # validate query string

    # request streams from Peloton Server

    # sort, and merge streams

    # cache merge stream

    # return next cached value
    return 'yes'

# Execute: run application directly, instead of import
if __name__ == '__main__':
    app.run(
    debug=True
)
