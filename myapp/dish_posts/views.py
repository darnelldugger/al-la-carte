from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import DishPost
from myapp.dish_posts.forms import DishPostForm

dish_posts = Blueprint('dish_posts', __name__)

@dish_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_dish():
    form = DishPostForm()
    if form.validate_on_submit():
        dish_post = DishPost(title=form.title.data, price=form.price.data, description=form.description.data, photo=form.photo.file, user_id=current_user.id)
        db.session.add(dish_post)
        db.session.commit()
        flash('Dish Post Created')
        print('Dish post was created')
        return redirect(url_for('core.index'))
    return render_template('create_dish.html', form=form)

@dish_posts.route('/<int:dish_post_id>')
def dish_post(dish_post_id):
    dish_post = DishPost.query.get_or_404(dish_post_id) 
    return render_template('dish_post.html', title=dish_post.title, date=dish_post.date, post=dish_post)

@dish_posts.route('/<int:dish_post_id>/update',methods=['GET','POST'])
@login_required
def update(dish_post_id):
    dish_post = DishPost.query.get_or_404(dish_post_id)

    if dish_post.restaurant != current_user:
        abort(403)

    form = DishPostForm()

    if form.validate_on_submit():
        dish_post.title = form.title.data
        dish_post.price = form.price.data
        dish_post.description = form.description.data
        db.session.commit()
        flash('Dish Post Updated')
        return redirect(url_for('dish_posts.dish_post',dish_post_id=dish_post.id))

    elif request.method == 'GET':
        form.title.data = dish_post.title
        form.price.data = dish_post.price
        form.description.data = dish_post.description

    return render_template('create_dish.html',title='Updating',form=form)

@dish_posts.route('/<int:dish_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(dish_post_id):

    dish_post = DishPost.query.get_or_404(dish_post_id)
    if dish_post.restaurant != current_user:
        abort(403)

    db.session.delete(dish_post)
    db.session.commit()
    flash('Dish Post Deleted')
    return redirect(url_for('core.index'))