from wtforms import Form, SubmitField

class TimeStarter(Form):
    start = SubmitField(label='Start')
    
