from flask import Flask, render_template, url_for, redirect
import products_data

app = Flask(__name__)
cart_item = []


@app.route('/')
def homepage():
    return render_template('index.html', cart_empty=(len(cart_item) == 0))


@app.route('/products')
def products():
    products_list = products_data.retrieve_all_products()
    return render_template('templates/products.html', products_list=products_list, cart_empty=(len(cart_item) == 0))


@app.route('/cart')
def cart():
    return render_template('templates/cart.html', products_list=cart_item, cart_empty=(len(cart_item) == 0))


@app.route('/add_product_to_cart/<product_id>')
def add_product_to_cart(product_id):
    if products_data.retrieve_requested_product(product_id) not in cart_item:
        cart_item.append(products_data.retrieve_requested_product(product_id))
    return redirect(url_for('products'))


@app.route('/remove_product_from_cart/<product_id>')
def remove_product_from_cart(product_id):
    cart_item.remove(products_data.retrieve_requested_product(product_id))
    return redirect(url_for('cart'))


@app.route('/products/<product_id>')
def show_product_details(product_id):
    product_details = products_data.retrieve_requested_product(product_id)
    return render_template('templates/product_details.html', product_details=product_details, cart_empty=(len(cart_item) == 0))


if __name__ == '__main__':
    app.run()
