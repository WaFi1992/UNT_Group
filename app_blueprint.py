from flask import Blueprint

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/')
def index():
    return "<h1>Homepage</h1>"

@app_blueprint.route('/about')
def about():
    return "<h1>about</h1>"

@app_blueprint.route('/contact')
def contact():
    return "<h1>Contact</h1>"