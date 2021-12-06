from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search_queries = StringField("Keyword: key1, Username: username, Verified: True, Retweet: True", validators=[DataRequired()])
    submit = SubmitField('Search')