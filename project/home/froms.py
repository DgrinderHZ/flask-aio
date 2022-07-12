from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(6, 80)])
    description = StringField("Description", validators=[DataRequired(), Length(max=200)])
