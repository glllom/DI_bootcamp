import json
from flask import Flask, render_template, redirect, url_for
from form import SearchForm
from config import Config

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)


def get_form():
    search_form = SearchForm()
    search_form.search_type.choices = ["By Name", "By Category"]
    return search_form


@app.route('/', methods=['GET', 'POST'])
def homepage():
    search_form = get_form()
    if search_form.is_submitted():
        if search_form.search_type.data == "By Name":
            return redirect(url_for('show_product_details', product_id=search_form.word.data))
        if search_form.search_type.data == "By Category":
            return redirect(url_for('products_by_category', product_category=search_form.word.data))
    return render_template('index.html', search_form=search_form)


@app.route('/products', methods=['GET', 'POST'])
def products():
    search_form = get_form()
    if search_form.is_submitted():
        if search_form.search_type.data == "By Name":
            return redirect(url_for('show_product_details', product_id=search_form.word.data))
        if search_form.search_type.data == "By Category":
            return redirect(url_for('products_by_category', product_category=search_form.word.data))
    with open('product_db.json', 'r') as f:
        products_list = json.load(f)
    return render_template('products.html', products_list=products_list, search_form=search_form)


@app.route('/products/category/<string:product_category>', methods=['GET', 'POST'])
def products_by_category(product_category):
    search_form = get_form()
    if search_form.is_submitted():
        if search_form.search_type.data == "By Name":
            return redirect(url_for('show_product_details', product_id=search_form.word.data))
        if search_form.search_type.data == "By Category":
            return redirect(url_for('products_by_category', product_category=search_form.word.data))
    with open('product_db.json', 'r') as f:
        all_products = json.load(f)
        products_list = []
    for product in all_products:
        if product['Category'] == product_category:
            products_list.append(product)
    return render_template('products.html', products_list=products_list, search_form=search_form)


@app.route('/products/<string:product_id>', methods=['GET', 'POST'])
def show_product_details(product_id):
    search_form = get_form()
    if search_form.is_submitted():
        if search_form.search_type.data == "By Name":
            return redirect(url_for('show_product_details', product_id=search_form.word.data))
        if search_form.search_type.data == "By Category":
            return redirect(url_for('products_by_category', product_category=search_form.word.data))
    product_details = {}
    with open('product_db.json', 'r') as f:
        for product in json.load(f):
            if product["ProductId"] == product_id:
                product_details = product
        if product_details == {}:
            return redirect('/')
    return render_template('product_details.html', product_details=product_details, search_form=search_form)



if __name__ == '__main__':
    app.run()

