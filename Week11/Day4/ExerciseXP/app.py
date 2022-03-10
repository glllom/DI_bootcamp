import json

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
def homepage():
    return render_template('index.html')


@app.route('/products')
def products():
    with open('product_db.json', 'r') as f:
        products_list = json.load(f)
    return render_template('products.html', products_list=products_list)


@app.route('/products/<string:product_id>')
def show_product_details(product_id):
    product_details = {}
    with open('product_db.json', 'r') as f:
        for product in json.load(f):
            if product["ProductId"] == product_id:
                product_details = product
    return render_template('product_details.html', product_details=product_details)


if __name__ == '__main__':
    app.run()
