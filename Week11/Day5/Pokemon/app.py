from flask import Flask, render_template, url_for, redirect, request, flash
import requests

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def get_types():
    pokemons_types = (requests.get("https://pokeapi.co/api/v2/type")).json()['results']
    return render_template('index.html', pokemons_types=pokemons_types)


@app.route('/pokemons/bytype', methods=['GET', 'POST'])
@app.route('/pokemons/bytype/<pokemon_type>')
def get_pokemons_by_type(pokemon_type=''):
    if request.method == 'POST':
        pokemon_type = request.form.get('search_by_type').lower()
        if pokemon_type == '' or pokemon_type is None:
            flash("Please enter the type")
            return redirect(url_for('get_types'))
    response = requests.get(f"https://pokeapi.co/api/v2/type/{pokemon_type}")
    if response.status_code == 200:
        pokemons_by_type = response.json()['pokemon']
        return render_template('bytype.html', pokemons_by_type=pokemons_by_type, pokemon_type=pokemon_type)
    flash("There are no pokemon with this type")
    return redirect(url_for('get_types'))


@app.route('/pokemons/byname', methods=['GET', 'POST'])
@app.route('/pokemons/byname/<pokemon_name>')
def check_if_exists(pokemon_name=''):
    if request.method == 'POST':
        pokemon_name = request.form.get('search_pokemon').lower()
        if pokemon_name == '' or pokemon_name is None:
            flash("Please enter the name")
            return redirect(url_for('get_types'))
    response = (requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"))
    if response.status_code == 200:
        return redirect(url_for('pokemon_information', id=pokemon_name))
    flash("There is no pokemon with this name")
    return redirect(url_for('get_all_pokemons'))


@app.route('/pokemon/<id>')
def pokemon_information(id):
    pokemon_dict = (requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")).json()
    pokemon = {'type': pokemon_dict['types'][0]['type']['name']
               }
    return render_template('pokemon_info.html', pokemon=pokemon, pokemon_dict=pokemon_dict)


@app.route('/pokemons/all')
def get_all_pokemons():
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 0
    count = (requests.get("https://pokeapi.co/api/v2/pokemon")).json()['count']
    limit = 20
    pokemons_list = (requests.get(f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={page}")).json()['results']
    return render_template('all_pokemons.html', pokemons_list=pokemons_list, offset=page)


if __name__ == '__main__':
    app.run()
