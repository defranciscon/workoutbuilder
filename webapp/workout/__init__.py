from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_module(app, **kwargs):
    
    csrf.init_app(app)
    
    from .controllers import workout_blueprint
    app.register_blueprint(workout_blueprint)
    
