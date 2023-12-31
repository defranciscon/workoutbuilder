
def create_module(app, **kwargs):
    from .controllers import timer_blueprint
    app.register_blueprint(timer_blueprint)
    
