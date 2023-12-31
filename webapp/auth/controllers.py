from flask import (render_template,
                   Blueprint,
                   redirect,
                   url_for,
                   flash,
                   jsonify)
from flask_login import login_user, logout_user, login_required
from flask_jwt_extended import create_access_token
from . import bcrypt, request, current_user, authenticate
from .models import User
from .forms import Login, Registration

auth_blueprint = Blueprint(
    'auth',__name__,
    template_folder='../templates/auth',
    url_prefix="/auth"
)

@auth_blueprint.route('/api', methods=["POST"])
def api():
    if not request.is_json:
        return jsonify({"msg":"Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    user = authenticate(username, password)
    if not user:
        return jsonify({"msg": "Bad username or password"}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
    
@auth_blueprint.route('/')
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in', 'info')
        return redirect(url_for('workout.home'))
    
    form = Login(request.form)
    
    if request.method == "POST" and form.validate():
        password = form.password.data
        user = User.objects(username__=form.username.data).first()
        
        if user is not None and user.check_password(password=password):
            login_user(user)
            flash(f"Welcome {user.firstname}!", 'success')
            return redirect(url_for('workout.home'))
        else:
            flash('(username) + password combination not found. Please try again.', 'error')
            
    return render_template('login.html', form=form)
    
@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_blueprint.route('/register', methods=['GET','POST'])
def register():
    form = Registration(request.form)
    if request.method == 'POST' and form.validate():
        
        existing_user = User.objects(username__iexact=form.username.data).first()
        if existing_user:
            flash('User already exists. Please try again.', 'danger')
            return redirect(url_for('auth.register'))
        
        password_hash=bcrypt.generate_password_hash(form.password.data)
        user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data, 
            email=form.email.data,
            username=form.username.data,
            password=password_hash
            )
        user.save()
        flash('You are now registered! Please proceed to login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html', form=form)