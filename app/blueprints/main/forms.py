
rom flask.ext.wtf import Form
from wtforms import BooleanField, SubmitField


class UpdateForm(Form):
    confirm = BooleanField('confirm')
    submit = SubmitField()
