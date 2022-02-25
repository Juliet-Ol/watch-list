from flask_wtf import FlaskForm #help create form class
from wtforms import StringField,TextAreaField,SubmitField #create
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):

    title = StringField('Review title', validators=[DataRequired()])
    review = TextAreaField('Movie review', validators=[DataRequired()])
    submit = SubmitField('Submit')