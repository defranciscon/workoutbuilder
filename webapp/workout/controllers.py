from flask import (render_template, 
                   Blueprint, flash, jsonify, 
                   redirect, 
                   url_for, 
                   current_app, 
                   abort, 
                   request)


from webapp import api
from webapp.auth import current_user
from webapp.auth.models import User
from webapp.workout.forms import WorkoutForm
from webapp.workout.models import Workout
from .engine.circuit import Circuit
from .engine.exercises import Exercise


workout_blueprint = Blueprint(
    'workout',__name__,
    template_folder='../templates/workout',
    url_prefix="/workout"
    )

@workout_blueprint.route('/home')
def home():
    return render_template('home.html')


@workout_blueprint.route('/edt', methods=['GET', 'POST'])
def new_edt():
    
    form = WorkoutForm()

    form.exercise_1.choices = [i for i in Exercise().get_upper_push()]
    form.exercise_2.choices = [i for i in Exercise().get_lower_gluteham()]
    form.exercise_3.choices = [i for i in Exercise().get_upper_pull()]
    form.exercise_4.choices = [i for i in Exercise().get_lower_quad()]
    form.exercise_5.choices = [i for i in Exercise().get_total_body()]
    form.exercise_6.choices = [i for i in Exercise().get_core_exercises()]
    form.exercise_7.choices = [i for i in Exercise().get_upper_pull()]
    form.exercise_8.choices = [i for i in Exercise().get_total_body()]
    
    if request.method == 'POST':
        
        title = request.form['title']
        block = request.form['block']
        reps = request.form['reps']
        
        exercise_1 = request.form['exercise_1']
        exercise_2 = request.form['exercise_2']
        exercise_3 = request.form['exercise_3']
        exercise_4 = request.form['exercise_4']
        exercise_5 = request.form['exercise_5']
        exercise_6 = request.form['exercise_6']
        exercise_7 = request.form['exercise_7']
        exercise_8 = request.form['exercise_8']
        
        circuit = Circuit()
        circuit.set_block(block)
        circuit.set_reps(reps)
        circuit.set_interval('NONE')
        circuit.set_rounds('NONE')
        circuit.store_exercises(exercise_1, exercise_2)
        circuit.store_exercises(exercise_3, exercise_4)
        circuit.store_exercises(exercise_5, exercise_6)
        circuit.store_exercises(exercise_7, exercise_8)
        
        workout = Workout(title, 'EDT')
        
        workout.create_workout(circuit=circuit.options)
        
        return redirect(url_for('workout.home'))
    
    return render_template('edt.html', form=form)


@workout_blueprint.route('/tabata', methods=['GET', 'POST'])
def new_tabata():
    
    form = WorkoutForm()

    form.exercise_1.choices = [i for i in Exercise().get_upper_push()]
    form.exercise_2.choices = [i for i in Exercise().get_total_body()]
    form.exercise_3.choices = [i for i in Exercise().get_core_exercises()]
    form.exercise_4.choices = [i for i in Exercise().get_total_body()]
    form.exercise_5.choices = [i for i in Exercise().get_total_body()]
    form.exercise_6.choices = [i for i in Exercise().get_upper_pull()]
    form.exercise_7.choices = [i for i in Exercise().get_total_body()]
    form.exercise_8.choices = [i for i in Exercise().get_core_exercises()]
    
    if request.method == 'POST':
        
        title = request.form['title']
        
        exercise_1 = request.form['exercise_1']
        exercise_2 = request.form['exercise_2']
        exercise_3 = request.form['exercise_3']
        exercise_4 = request.form['exercise_4']
        exercise_5 = request.form['exercise_5']
        exercise_6 = request.form['exercise_6']
        exercise_7 = request.form['exercise_7']
        exercise_8 = request.form['exercise_8']
        
        circuit = Circuit()
        circuit.set_block('NONE')
        circuit.set_reps('NONE')
        circuit.set_interval('20:10')
        circuit.set_rounds('4 rounds')
        circuit.store_exercises(exercise_1, exercise_2)
        circuit.store_exercises(exercise_3, exercise_4)
        circuit.store_exercises(exercise_5, exercise_6)
        circuit.store_exercises(exercise_7, exercise_8)
        
        workout = Workout(title, 'TABATA')
        
        workout.create_workout(circuit=circuit.options)
        
        return redirect(url_for('workout.home'))
    
    return render_template('tabata.html', form=form)


@workout_blueprint.route('/sequential', methods=['GET', 'POST'])
def new_sequential():
    
    form = WorkoutForm()

    form.exercise_1.choices = [i for i in Exercise().get_upper_push()]
    form.exercise_2.choices = [i for i in Exercise().get_lower_gluteham()]
    form.exercise_3.choices = [i for i in Exercise().get_upper_pull()]
    form.exercise_4.choices = [i for i in Exercise().get_lower_quad()]
    form.exercise_5.choices = [i for i in Exercise().get_total_body()]
    form.exercise_6.choices = [i for i in Exercise().get_core_exercises()]
    form.exercise_7.choices = [i for i in Exercise().get_upper_pull()]
    form.exercise_8.choices = [i for i in Exercise().get_total_body()]
    form.exercise_9.choices = [i for i in Exercise().get_upper_pull()]
    form.exercise_10.choices = [i for i in Exercise().get_total_body()]
    
    form.interval.choices = [
        ('20:10', '20 sec work, 10 sec rest'), 
        ('30:15', '30 sec work, 15 sec rest'),
        ('40:20', '40 sec work, 20 sec rest'), 
        ('45:15', '45 sec work, 15 sec rest'), 
        ('50:10', '50 sec work, 10 sec rest')
    ]
    
    if request.method == 'POST':
        
        title = request.form['title']
        interval = request.form['interval']
        
        exercise_1 = request.form['exercise_1']
        exercise_2 = request.form['exercise_2']
        exercise_3 = request.form['exercise_3']
        exercise_4 = request.form['exercise_4']
        exercise_5 = request.form['exercise_5']
        exercise_6 = request.form['exercise_6']
        exercise_7 = request.form['exercise_7']
        exercise_8 = request.form['exercise_8']
        exercise_9 = request.form['exercise_9']
        exercise_10 = request.form['exercise_10']
        
        circuit = Circuit()
        circuit.set_block('NONE')
        circuit.set_reps('NONE')
        circuit.set_interval(interval)
        circuit.set_rounds('2 rounds')
        circuit.store_exercises(
            exercise_1, exercise_2, exercise_3, exercise_4, exercise_5,
            exercise_6, exercise_7, exercise_8, exercise_9, exercise_10)
        
        workout = Workout(title, 'SEQ')
        
        workout.create_workout(circuit=circuit.options)
        
        return redirect(url_for('workout.home'))
    
    return render_template('sequential.html', form=form)


@workout_blueprint.route('/undulating', methods=['GET', 'POST'])
def new_undulating():
    
    form = WorkoutForm()

    form.exercise_1.choices = [i for i in Exercise().get_upper_push()]
    form.exercise_2.choices = [i for i in Exercise().get_lower_gluteham()]
    form.exercise_3.choices = [i for i in Exercise().get_upper_pull()]
    form.exercise_4.choices = [i for i in Exercise().get_lower_quad()]
    form.exercise_5.choices = [i for i in Exercise().get_total_body()]
    form.exercise_6.choices = [i for i in Exercise().get_core_exercises()]
    form.exercise_7.choices = [i for i in Exercise().get_upper_pull()]
    form.exercise_8.choices = [i for i in Exercise().get_total_body()]
    
    form.interval.choices = [
        ('20:10', '20 sec work, 10 sec rest'), 
        ('30:15', '30 sec work, 15 sec rest'),
        ('40:20', '40 sec work, 20 sec rest'), 
        ('45:15', '45 sec work, 15 sec rest'), 
        ('50:10', '50 sec work, 10 sec rest')
    ]
    
    form.rounds.choices = [
        ('2 rounds', 2),
        ('4 rounds', 4),
        ('6 rounds', 6)
    ]
    
    if request.method == 'POST':
        
        title = request.form['title']
        interval = request.form['interval']
        rounds = request.form['rounds']
        
        
        exercise_1 = request.form['exercise_1']
        exercise_2 = request.form['exercise_2']
        exercise_3 = request.form['exercise_3']
        exercise_4 = request.form['exercise_4']
        exercise_5 = request.form['exercise_5']
        exercise_6 = request.form['exercise_6']
        exercise_7 = request.form['exercise_7']
        exercise_8 = request.form['exercise_8']
        
        circuit = Circuit()
        circuit.set_block('NONE')
        circuit.set_reps('NONE')
        circuit.set_interval(interval)
        circuit.set_rounds(rounds)
        circuit.store_exercises(exercise_1, exercise_2)
        
        circuit_1 = Circuit()
        circuit_1.set_block('NONE')
        circuit_1.set_reps('NONE')
        circuit_1.set_interval(interval)
        circuit_1.set_rounds(rounds)
        circuit_1.store_exercises(exercise_3, exercise_4)
        
        circuit_2 = Circuit()
        circuit_2.set_block('NONE')
        circuit_2.set_reps('NONE')
        circuit_2.set_interval(interval)
        circuit_2.set_rounds(rounds)
        circuit_2.store_exercises(exercise_5, exercise_6)
        
        circuit_3 = Circuit()
        circuit_3.set_block('NONE')
        circuit_3.set_reps('NONE')
        circuit_3.set_interval(interval)
        circuit_3.set_rounds(rounds)
        circuit_3.store_exercises(exercise_7, exercise_8)
        
        workout = Workout(title, 'UND')
        
        workout.create_workout(
            circuit_0=circuit.options,
            circuit_1=circuit_1.options,
            circuit_2=circuit_2.options,
            circuit_3=circuit_3.options
            )
        
        return redirect(url_for('workout.home'))
    
    return render_template('undulating.html', form=form)