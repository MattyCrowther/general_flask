from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms import FileField
from wtforms import validators

class UploadForm(FlaskForm):
    class Meta:
        csrf = False
    submit_upload = SubmitField('Submit')
    upload = FileField('Upload File', validators=[validators.InputRequired()])

class PasteForm(FlaskForm):
    class Meta:
        csrf = False
    submit_paste = SubmitField('Submit')
    paste = TextAreaField('Paste', validators=[validators.InputRequired()])