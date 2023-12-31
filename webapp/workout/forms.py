from wtforms import (   
                     Form,
                     FormField,
                     StringField, 
                     SelectField, 
                     RadioField, 
                     SubmitField, 
                     validators,
                     FieldList
                        )     
from flask_wtf import FlaskForm


class WorkoutForm(FlaskForm):
    
    title = StringField(label='Title', validators=[validators.DataRequired()])
    
    block = SelectField(label='Block Time', choices=[
        ('4 min' ,  4),
        ('5 min' ,  5),
        ('6 min' ,  6),
        ('8 min' ,  8),
        ('10 min', 10)])
    
    reps = SelectField(label='Reps Per Set', choices=[
        ('6 reps', 6), ('8 reps', 8), ('10 reps', 10), ('12 reps', 12)], coerce=str)
    
    interval = SelectField(label='Interval', coerce=str)
    
    rounds = SelectField(label='Rounds', coerce=str)
    
    exercise_1 = SelectField(label='Exercise', coerce=str, validators=[validators.DataRequired()])
    exercise_2 = SelectField(label='Exercise', coerce=str, validators=[validators.DataRequired()])
    exercise_3 = SelectField(label='Exercise', coerce=str, validators=[validators.DataRequired()])
    exercise_4 = SelectField(label='Exercise', coerce=str, validators=[validators.DataRequired()])
    exercise_5 = SelectField(label='Exercise', coerce=str, validators=[validators.DataRequired()])
    exercise_6 = SelectField(label='Exercise', coerce=str, validators=[validators.DataRequired()])
    exercise_7 = SelectField(label='Exercise', coerce=str, validators=[validators.DataRequired()])
    exercise_8 = SelectField(label='Exercise', coerce=str, validators=[validators.DataRequired()])
    exercise_9 = SelectField(label='Exercise', coerce=str, validators=[validators.DataRequired()])
    exercise_10 = SelectField(label='Exercise', coerce=str, validators=[validators.DataRequired()])
    
    submit = SubmitField(label='Submit', validators=[validators.DataRequired()])
    
class UndulatingWorkoutForm(WorkoutForm):
    
    interval_1 = SelectField(label='Interval', coerce=str)
    interval_2 = SelectField(label='Interval', coerce=str)
    interval_3 = SelectField(label='Interval', coerce=str)
    interval_4 = SelectField(label='Interval', coerce=str)
    
    rounds_1 = SelectField(label='Rounds', coerce=str)
    rounds_2 = SelectField(label='Rounds', coerce=str)
    rounds_3 = SelectField(label='Rounds', coerce=str)
    rounds_4 = SelectField(label='Rounds', coerce=str)
    
    
    
    
    
    
    
    
    