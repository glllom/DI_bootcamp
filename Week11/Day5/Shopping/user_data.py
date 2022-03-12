import json


def add_user(username, email, password):
    with open('data/users.json', 'a') as f:
        user = {'username': username, 'email': email, 'password': password}
        json.dump(user, f, indent=4)


def check_user(username):
    with open('data/users.json', 'a') as f:
        users = json.load(f)
        return username in [lambda user: user['username'] for user in users]





add_user('gleb', 'asd@asd.sd', '123')