# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import DishPost

core = Blueprint('core', __name__)

@core.route('/')
def index():
    dish_posts = DishPost.query.order_by(DishPost.date.desc())
    return render_template('index.html', dish_posts=dish_posts)

@core.route('/info')
def info():
    return render_template('info.html')