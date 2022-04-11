#models 
from enum import unique
from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
#allows to set up isAuthenticate etc 
from flask_login import UserMixin
from datetime import datetime

#login management 
# allows us to use this in templates for isUser stuff 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), unique=True, index=True)
    lastname = db.Column(db.String(64), unique=True, index=True)
    restaurantname = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('DishPost', backref='restaurant', lazy=True)

    def __init__(self, firstname, lastname, restaurantname, email, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.restaurantname = restaurantname
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

#going to use this in our login view 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"

class DishPost(db.Model):
    __tablename__ = 'dish_posts'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def __init__(self, title, price, description, user_id):
        self.title = title
        self.price = price
        self.description = description
        self.user_id = user_id


    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- Title: {self.Title}"
