from flask_restful import Api
from .workout.controllers import WorkoutApi

rest_api = Api()

def create_module(app, **kwargs):
    
    rest_api.add_resource(
        WorkoutApi,
        '/api/workout',
        '/api/workout/<string:id>'
    )
    rest_api.init_app(app)
    