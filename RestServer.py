#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import abort
from flask import make_response
import json
import datamuse

app = Flask(__name__)

# example request:
# curl -i -H "Content-Type: application/json" -X POST -d '{"ml":"Seasoning on an everything bagel"}' http://localhost:5000/datamuse/api/search_datamuse_wordenp
@app.route('/datamuse/search_datamuse_wordenp', methods=['POST'])
def search_wordenp():
    if not request.json or not 'ml' in request.json:
        abort(400)
    result = datamuse.search_datamuse_wordenp(request.json['ml'])
    return json.dumps(result) + "\n", 200

# example request:
# curl -i -H "Content-Type: application/json" -X POST -d '{"ml":"Seasoning on an everything bagel"}' http://localhost:5000/datamuse/api/wiki_search
@app.route('/datamuse/wiki_search', methods=['POST'])
def wiki_search():
    if not request.json or not 'ml' in request.json:
        abort(400)
    result = datamuse.wiki_search(request.json['ml'])
    return json.dumps(result) + "\n", 200

# example request:
# curl -i -H "Content-Type: application/json" -X POST -d '{"ml":"Seasoning on an everything bagel", "word_length": 4}' http://localhost:5000/datamuse/api/datamuse_answer_list
@app.route('/datamuse/datamuse_answer_list', methods=['POST'])
def answer_list():
    if not request.json or not 'ml' in request.json or not 'word_length' in request.json:
        abort(400)
    result = datamuse.datamuse_answer_list(request.json['ml'], request.json['word_length'])
    return json.dumps(result) + "\n", 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(debug=True)