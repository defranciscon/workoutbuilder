from wtforms import Form, StringField, PasswordField, SubmitField, validators

class Registration(Form):
    firstname = StringField(label='First Name', validators=[validators.Length(min=2, max=25)])
    lastname = StringField(label='Last Name', validators=[validators.Length(min=2, max=25)])
    email = StringField(label='Email', validators=[validators.Length(min=6, max=35)])
    username = StringField(label='Username', validators=[validators.Length(min=2, max=35)])
    password = PasswordField(label='New Password', validators=[
        validators.Length(min=8, max=35),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField(label='Register')
    
class Login(Form):
    username = StringField(label='Username', validators=[validators.Length(min=2, max=25)])
    password = PasswordField(label='Password', validators=[
        validators.Length(min=8, max=35),
        validators.DataRequired()])
    submit = SubmitField(label='Login')
