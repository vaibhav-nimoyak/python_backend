from flask import Flask, request, jsonify, render_template
# from helper import product
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


@app.route('/math/add', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({'result': data['a'] + data['b']})

@app.route('/math/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    return jsonify({'result': data['a'] - data['b']})

@app.route('/math/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    return jsonify({'result': data['a'] * data['b']})

@app.route('/math/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if data['b'] == 0:
        return jsonify({'message': 'Cannot divide by zero'}), 400
    return jsonify({'result': data['a'] / data['b']}), 200

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    if data['name'] == '':
        return jsonify({'message': 'Please enter your name'}), 400
    return jsonify({'message': f'Hello, {data["name"]}!'}), 200

@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    success, product = (product(id))
    if success:
        return jsonify(product)
    else:
        return jsonify({'message': 'Product not found'}), 404

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    return jsonify({'text': data['text']}), 200

if __name__ == '__main__':
    app.run(port=5000,debug=True)