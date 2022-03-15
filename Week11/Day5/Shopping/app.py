import json
from flask import Flask, render_template, url_for, redirect, request, flash
import products_data
import user_data

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
cart_item = []
logged_user = False


@app.route('/', methods=['GET', 'POST'])
def homepage():
    global logged_user
    global cart_item
    print('logged_user', logged_user)
    log_out = request.args.get('log_out')
    if log_out:
        cart_item = []
        logged_user = False
        return redirect(url_for('homepage'))
    if request.method == 'GET':
        return render_template('index.html', cart_empty=(len(cart_item) == 0), logged_user=logged_user)
    #  log in
    if user := request.form.get("login-user"):
        password = request.form.get("login-password")
        if user and password and user_data.check_user(user):
            if user_data.check_password(user.lower(), password):
                logged_user = user
                cart_item = user_data.get_cart(user)
                print('logged')
                return redirect(url_for('homepage'))
            else:
                print('incorrect password')
                flash("Incorrect password")
        flash("Login failed")
        print('login failed')
    # sign up
    if user := request.form.get("signup-user"):
        print('Stage', user)
        password = request.form.get("signup-password")
        email = request.form.get("signup-email")
        if "" in [user, password, email]:
            flash("All fields must contain values.")
        elif user_data.check_user(user.lower()):
            flash("This username already exists.")
        else:
            user_data.add_user(user.lower(), email, password)
            logged_user = user
    return redirect(url_for('homepage'))


@app.route('/products')
def products():
    products_list = products_data.retrieve_all_products()
    return render_template('products.html', products_list=products_list, cart_empty=(len(cart_item) == 0), logged_user=logged_user)


@app.route('/cart')
def cart():
    return render_template('cart.html', products_list=cart_item, cart_empty=(len(cart_item) == 0), logged_user=logged_user)


@app.route('/add_product_to_cart/<product_id>')
def add_product_to_cart(product_id):
    if products_data.retrieve_requested_product(product_id) not in cart_item:
        cart_item.append(products_data.retrieve_requested_product(product_id))
        user_data.update_cart(logged_user, cart_item)
    return redirect(url_for('products'))


@app.route('/remove_product_from_cart/<product_id>')
def remove_product_from_cart(product_id):
    cart_item.remove(products_data.retrieve_requested_product(product_id))
    user_data.update_cart(logged_user, cart_item)
    return redirect(url_for('cart'))


@app.route('/products/<product_id>')
def show_product_details(product_id):
    product_details = products_data.retrieve_requested_product(product_id)
    return render_template('product_details.html', product_details=product_details, cart_empty=(len(cart_item) == 0), logged_user=logged_user)


if __name__ == '__main__':
    app.run()

