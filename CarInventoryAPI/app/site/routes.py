from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/user_cars')
def user_cars():
    return render_template('user_cars.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')