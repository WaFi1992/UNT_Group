from datetime import datetime
from bookapp import db, loginManager
from flask_login import UserMixin

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),
                           nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    payment_profile = db.Column(db.String(60))
    major = db.Column(db.String(20))
    posts = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    title = db.Column(db.Text, nullable=False)
    publisher = db.Column(db.Text, nullable=False)
    writers = db.Column(db.Text, nullable=False)
    image_ref = db.Column(db.String(120), nullable=False, default='book.jpg')
    condition = db.Column(db.Text, nullable=False)
    
    price = db.Column(db.String(60), nullable=False)
    major = db.Column(db.String(20))
    edition = db.Column(db.String(20))
    binding = db.Column(db.String(20))
    #comments = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title},')"


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment_text = db.Column(db.Text, nullable=False)
    comment_time = db.Column(db.DateTime, nullable=False, 
                    default=datetime.utcnow)
    posts_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title},')"
