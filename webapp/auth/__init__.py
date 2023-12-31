from flask import flash, redirect, url_for, session, abort, request
from flask_login import current_user
from flask_login import LoginManager, login_user
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
jwt = JWTManager()

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"

def create_module(app, **kwargs):
    bcrypt.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)
    
    from .controllers import auth_blueprint
    app.register_blueprint(auth_blueprint)
    
def authenticate(username, password):
    from .models import User
    user = User.objects(username__=username).first()
    if not user:
        return None
    if not user.check_password(password):
        return None
    return user

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.objects(pk=user_id).first()

