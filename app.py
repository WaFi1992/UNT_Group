from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app_blueprint import app_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite::///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    payment_profile = db.Column(db.String(60))
    major = db.Column(db.String(20))
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.Text, nullable=False)
    publisher = db.Column(db.Text, nullable=False)
    writers = db.Column(db.Text, nullable=False)
    image_ref = db.Column(db.String(120), nullable=False, default='book.jpg')
    condition = db.Column(db.Text, nullable=False)
    price = db.Column(db.String(60), nullable=False)
    major = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title},')"

app.register_blueprint(app_blueprint)

