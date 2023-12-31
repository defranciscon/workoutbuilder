from flask import (render_template, 
                   Blueprint, 
                   flash, 
                   redirect, 
                   url_for, 
                   current_app, 
                   session, 
                   request)
from webapp import api
from webapp.timer.forms import TimeStarter
from webapp.timer.interval import IntervalTimer

timer_blueprint = Blueprint(
    'timer',__name__,
    template_folder='../templates/workout/timer',
    url_prefix="/timer"
    )

@timer_blueprint.route("/timer")
def init_timer():
    form = TimeStarter(request.form)
    if form.validate():
        start = form.start.data
        timer = IntervalTimer(20, 10, 4, 60, 1)
        if start:
            timer.run_circuit()
    return render_template("timer.html")





