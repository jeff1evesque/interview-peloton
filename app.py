## @app.py
# This file loads corresponding logic, and html template file(s), which
#     allows the presentation of (asynchronous) content.
import json
from flask import Flask, render_template, request

# Initialize: create flask instance
app = Flask(__name__)

# index: define HTML template for base URL
@app.route('/')
def index():
    return render_template('index.html')

## quiz_merge: main logic
@app.route('/quiz/merge', methods=['POST', 'GET'])
def quiz():

    # validate query string

    # request streams from Peloton Server

    # sort, and merge streams

    # cache merge stream

    # return next cached value
    return

# Execute: run application directly, instead of import
if __name__ == '__main__':
    app.run(
    debug=True
)
