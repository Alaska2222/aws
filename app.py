from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy data for products
products = [
    {"id": 1, "name": "Product 1", "price": 20},
    {"id": 2, "name": "Product 2", "price": 30},
    {"id": 3, "name": "Product 3", "price": 30}
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    return jsonify({"message": f"Product {product_id} added to cart!"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
