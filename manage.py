import os
from webapp import client, create_app
from webapp.workout.models import Workout
from webapp.auth.models import User

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=client, User=User, Workout=Workout)

