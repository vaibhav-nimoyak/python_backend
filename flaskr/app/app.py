from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', title='Home')

@app.route('/about', methods=['GET'])
def about():
    return jsonify({'message': 'About page'})

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    return jsonify({'message': f'Hello, {data["name"]}!'})

@app.route('/math', methods=['GET'])
def math():
    a = request.args.get('a')
    b = request.args.get('b')
    return jsonify({'result': int(a) + int(b)})

app.run(port=5000)