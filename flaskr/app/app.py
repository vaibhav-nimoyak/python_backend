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

@app.route('/form', methods=['GET'])
def form_page():
    return render_template('form.html', name="Developer")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello, {name}!"

# TODO: Add a route for the contact page
@app.route('/contact', methods=['GET'])
def contact_page():
    return render_template('contact.html')

#TODO: Add a route for the customer service page
@app.route('/customer_service', methods=['POST'])
def customer_service():
    """Handle form submission"""
    pass


app.run(port=5000)