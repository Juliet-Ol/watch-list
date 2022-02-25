from turtle import title
from flask_wtf import FlaskForm #help create form class
from wtforms import StringField,TextAreaField,SubmitField #create
from wtforms.validators import Required #validator

class ReviewForm(FlaskForm):

    title = StringField('Review title', validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit - SubmitField('Submit')