from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField
# other fields include PasswordField
from wtforms.validators import Required, Email

class ContactForm(Form):
    name = TextField('Name')
    email = TextField('E-Mail', validators=[Required(), Email()])
    subject = TextField('Subject',validators=[Required()])
    message = TextAreaField('Message',validators=[Required()])

