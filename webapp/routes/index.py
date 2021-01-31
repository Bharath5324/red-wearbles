from webapp import WEBAPP
from app.models import Institution
from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_user, login_required, logout_user
@WEBAPP.route('/')
def index():
    role = False
    if current_user.is_authenticated:
        if Institution.query.filter_by(login_id=current_user.id).first():
            role = True
    return render_template('index.html', role=role)


