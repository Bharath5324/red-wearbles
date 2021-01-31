from api import API_APP
from flask import render_template
from flask_login import current_user
from .auth import authorization_required
from app.models import User, instit_scan
from app.firebase import fire
@API_APP.route('/dashboard')
@authorization_required
def dashboard():
    user = User.query.filter_by(login_id=current_user.id).first()
    dashdat = fire("chipid", user.tagid)
    return render_template('u_dashboard.html', user=user, dashdat=dashdat, instit_scan=instit_scan)