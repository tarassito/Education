from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def test():
    return 'Hello, World!'

@app.route('/calc')
def calc():
    my_list = [x for x in range(10000)]
    return jsonify({'list': my_list})

app.run(host='0.0.0.0')
