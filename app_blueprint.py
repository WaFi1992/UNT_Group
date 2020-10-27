from flask import Blueprint, render_template, url_for

app_blueprint = Blueprint('app_blueprint', __name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app_blueprint.route('/')
def index():
    return render_template('home.html', posts=posts)


@app_blueprint.route('/about')
def about():
    return render_template('about.html')


@app_blueprint.route('/contact')
def contact():
    return "<h1>Contact</h1>"