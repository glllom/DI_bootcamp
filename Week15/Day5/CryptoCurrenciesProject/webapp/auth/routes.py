from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from webapp import db
from webapp.auth.models import User

auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


@auth.route('/login')
def login():
	return render_template('auth/login.html')


@auth.route('/')
def index():
	return "index"


@auth.route('/signup')
def signup():
	return render_template('auth/signup.html')