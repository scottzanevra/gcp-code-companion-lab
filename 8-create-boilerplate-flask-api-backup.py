
# create a boilerplate flask application with api's for a product catalog

import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a product catalog
products = [
    {
        "id": 1,
        "name": "Product 1",
        "description": "This is product 1.",
        "price": 10.00
    },
    {
        "id": 2,
        "name": "Product 2",
        "description": "This is product 2.",
        "price": 20.00
    },
    {
        "id": 3,
        "name": "Product 3",
        "description": "This is product 3.",
        "price": 30.00
    }
]

# Create a route to get all products
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

# Create a route to get a product by id
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found."}), 404

# Create a route to create a product
@app.route("/products", methods=["POST"])
def create_product():
    product = request.get_json()
    product["id"] = len(products) + 1
    products.append(product)
    return jsonify(product)

# Create a route to update a product
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        product.update(request.get_json())
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found."}), 404
