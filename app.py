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
    if request.method == 'GET':
        # validate query string
        stream_1 = request.args.get('stream1')
        stream_2 = request.args.get('stream2')

        if validate_alphanum(stream_1) and validate_alphanum(stream_2):
            # request streams from Peloton Server
            content_1 = get_content(stream_1)
            content_2 = get_content(stream_1)

            # cache stream

            # sort, and merge streams

            # return next cached value
        else:
            list_error.append('the provided \'stream1\', and \'stream2\' each need to be a alphanumeric string, without spaces or special characters.')
            return json.dumps({'status': 'error', 'result': None, 'error': list_error})
    else:
        error = 'Must provide valid \'GET\' request with \'stream1\', and \'stream2\' string parameters defined.'
        return json.dumps({'status': 'error', 'result': None, 'error': list_error})

# Execute: run application directly, instead of import
if __name__ == '__main__':
    app.run(
    debug=True
)
