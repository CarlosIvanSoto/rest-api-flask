from products import products
from flask import Flask, jsonify, request

app = Flask(__name__)
#default check rest api route
@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})
#get all products route
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"count": len(products),"message":"Product's list", "results": products})
#get product from name route
@app.route('/product/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if len(productFound) > 0:
        return jsonify({
            "count": len(productFound),
            "result":productFound,
            "message":"Product "+product_name
        })
    else:
        return jsonify({
            "message":"Product not found"
        })
#get product from index route
@app.route('/product/<int:index>', methods=['GET'])
def getProductForIndex(index):
    return jsonify({
        "result":products[index]
    })
#add products route
@app.route('/products/', methods=['POST'])
def addProducts():
    return jsonify({
        "Message": "Product Added Successfully", 
        "result": request.json
    })
# Update product from name route
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'result': productsFound[0]
        })
    return jsonify({
            'message': 'Product Not found'
        })

# DELETE product from name Route
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })
if __name__ == '__main__':
    app.run(debug=True, port=4000)