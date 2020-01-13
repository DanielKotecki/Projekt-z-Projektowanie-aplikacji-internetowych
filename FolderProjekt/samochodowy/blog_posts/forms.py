from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):
    title=StringField('Tytuł',validators=[DataRequired()])
    text=TextAreaField('Tekst',validators=[DataRequired()])
    submit=SubmitField('Wstaw')
