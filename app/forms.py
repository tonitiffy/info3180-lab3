from flask.ext.wtf import Form
from wtforms.fields import TextField
# other fields include PasswordField
from wtforms.validators import Required, Email

class ContactForm(Form):
    name = TextField('Please enter your full name')
    email = TextField('Please enter your full e-mail', validators=[Required()], Email()])
    subject = TextField(validators=[Required()])
    message = TextField('Please enter the message you want to send.',validators=[Required()])
