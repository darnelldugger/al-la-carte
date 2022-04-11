from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class DishPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Post')