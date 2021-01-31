from functools import wraps
from webapp import WEBAPP
from flask import redirect, url_for, render_template, request, flash
from flask_login import login_required, current_user, login_user, logout_user
from app.models import Institution, Login, signup_institute, delete_insit
from app.forms import LoginForm, InstituteSignupForm
@WEBAPP.route('/login', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('webapp.index'))
    form = LoginForm()
    if form.validate_on_submit():
        # print(form)
        login = Login.query.filter_by(email=form.email.data).first()
        # user = Institution.query.filter_by(login_id=login.id).first()
        if login is None or not login.check_password(form.password.data):
            flash('invalid username/password')
            return redirect(url_for('webapp.signin'))
        login_user(login, remember=form.rememberme.data)
        return redirect(url_for('webapp.index'))
    return render_template('login.html', form=form)

@WEBAPP.route('/logout')
def signout():
    logout_user()
    return redirect(url_for('webapp.index'))

@WEBAPP.route('/register', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('webapp.dashboard'))
    form = InstituteSignupForm()
    if form.validate_on_submit():
        print(form)
        signup_institute(form)
        flash("You have sucessfully registered", 'Success')
        return redirect(url_for('webapp.signin'))
    return render_template("signup.html", form=form)
def authorization_required(func):
    @wraps(func)    
    @login_required
    def inner(*args, **kwargs):
        if not Institution.query.filter_by(login_id=current_user.id):
            return redirect(url_for('webapp.index'))
        return func(*args, **kwargs)
    return inner

@WEBAPP.route('/delete', methods=['GET', 'POST'])
@login_required
def delete_acc():
    x = current_user.id
    logout_user()
    delete_insit(x)
    return redirect(url_for('webapp.index'))