from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import DishPost
from myapp.dish_posts.forms import DishPostForm

dish_posts = Blueprint('dish_posts', __name__)