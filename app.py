## @app.py
# This file loads corresponding logic, and html template file(s), which
#     allows the presentation of (asynchronous) content.
import json
from flask import Flask, render_template, request
from logic.validation import validate_alphanum
from logic.parser import get_content
from logic.cached_stream import cached_stream
from logic.utility import linear_merge
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
        # local variables
        list_stream_1 = []
        list_stream_2 = []

        # validate query string
        stream_1 = request.args.get('stream1')
        stream_2 = request.args.get('stream2')

        if validate_alphanum(stream_1) and validate_alphanum(stream_2):
            # request streams from Peloton Server
            content_1 = get_content(stream_1)['current']
            content_2 = get_content(stream_1)['current']

            # cache stream
            cache = cached_stream(content_1, content_2)
            cached_list_1 = cache['first']
            cached_list_2 = cache['second']

            # merge cached lists
            merged_streams = linear_merge(cached_list_1, cached_list_2)

            # return merged steams (list)
            return json.dumps(merged_streams)
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
