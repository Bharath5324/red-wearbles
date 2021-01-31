from functools import wraps
from api import API_APP
from app.forms import LoginForm, UserSignupForm
from app.models import User, Login, delete_user
from flask import redirect, url_for, flash, render_template
from flask_login import current_user, login_user, login_required, logout_user
from app.models import signup_user
@API_APP.route('/login', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('webapp.index'))
    form = LoginForm()
    if form.validate_on_submit():
        print(form)
        login = Login.query.filter_by(email=form.email.data).first()
        if login is None or not login.check_password(form.password.data):
            flash('invalid username/password')
            return redirect(url_for('api.signin'))
        user = User.query.filter_by(login_id=login.id).first()
        if user is None:
            flash('invalid username/password')
            return redirect(url_for('api.signin'))
        login_user(login, remember=form.rememberme.data)
        return redirect(url_for('webapp.index'))
    return render_template('u_login.html', form=form)


@API_APP.route('/register', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('webapp.dashboard'))
    form = UserSignupForm()
    if form.validate_on_submit():
        print(form)
        signup_user(form)
        flash("You have sucessfully registered", 'Success')
        return redirect(url_for('api.signin'))
    return render_template("u_signup.html", form=form)

def authorization_required(func):
    @wraps(func)    
    @login_required
    def inner(*args, **kwargs):
        if not User.query.filter_by(login_id=2):
            return redirect(url_for('webapp.index'))
        return func(*args, **kwargs)
    return inner

@API_APP.route('/delete', methods=['GET', 'POST'])
@login_required
def delete_acc():
    x = current_user.id
    logout_user()
    delete_user(x)
    return redirect(url_for('webapp.index'))