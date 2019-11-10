from flask import Flask, request
from snips_nlu import SnipsNLUEngine

app = Flask(__name__)

engine = SnipsNLUEngine.from_path('/nlu_engine/')


@app.route('/query', methods=['POST'])
def parse_query():
    query = request.form['query']
    intent = engine.parse(query)
    return intent


app.run(host='0.0.0.0')
