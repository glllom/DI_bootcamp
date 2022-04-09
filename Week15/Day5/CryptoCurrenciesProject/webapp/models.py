# sourcery skip: avoid-builtin-shadow
from webapp import db
from flask_login import UserMixin
from webapp.config import Api
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column("username", db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)


class CryptoCurrencies(db.Model):
    cripto_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column("name", db.String(32), unique=True)
    symbol = db.Column("symbol", db.String(32), unique=True)
    slug = db.Column("slug", db.String(32), unique=True)
    first_historical_data = db.Column("first_historical_data", db.String(32))
    last_historical_data = db.Column("last_historical_data", db.String(32))
    is_active = db.Column("is_active", db.Integer)

    def get_info(self):
        """Receives a cryptocurrency id from the table, and uses the API to fetch information about it."""
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': Api.CRIPTO_API
        }
        session = Session()
        session.headers.update(headers)
        try:
            response = session.get(url)
            data = json.loads(response.text)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            return
        for coin in data["data"]:
            if coin["id"] == self.cripto_id:
                return coin



# qqq = CryptoCurrencies()
# qqq.get_info()