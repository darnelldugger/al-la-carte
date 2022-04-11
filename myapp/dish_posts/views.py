from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import DishPost
from myapp.dish_posts.forms import DishPostForm

dish_posts = Blueprint('dish_posts', __name__)

@dish_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = DishPostForm()
    if form.validate_on_submit():
        dish_post = DishPost(title=form.title.data, price=form.price.data, description=form.description.data, user_id=current_user.id)
        db.session.add(dish_post)
        db.session.commit()
        flash('Dish Post Created')
        print('Dish post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)

@dish_posts.route('/<int:dish_post_id>')
def dish_post(dish_post_id):
    dish_post = DishPost.query.get_or_404(dish_post_id) 
    return render_template('dish_post.html', title=dish_post.title, date=dish_post.date, post=dish_post)