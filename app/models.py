from app import db
from datetime import datetime
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
class Login(UserMixin, db.Model):
    __tablename__ = "Login"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(200))
    institution = db.relationship('Institution', backref='login', lazy=True)
    user = db.relationship('User', backref='login', lazy=True)
    def __repr__(self):
        return '<User {}>'.format(self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Institution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.Integer, db.ForeignKey('Login.id'))
    kind = db.Column(db.String(64), nullable = False)
    scanner_id = db.Column(db.String(128), nullable = False, index=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.Integer, db.ForeignKey('Login.id'))
    contact1 = db.Column(db.BigInteger, nullable=False)
    contact2 = db.Column(db.BigInteger, nullable=False)
    contact3 = db.Column(db.BigInteger, nullable=False)
    contact4 = db.Column(db.BigInteger, nullable=False)
    url = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    group = db.Column(db.String(20), nullable=False)
    tagid = db.Column(db.String(50), nullable=False)

@login.user_loader
def load_user(id):
    return Login.query.get(int(id))

def signup_user(form):
    new_login = Login(name=form.name.data, email=form.email.data)
    new_login.set_password(form.password.data)
    db.session.add(new_login)
    db.session.commit()
    new_user = User(login_id=new_login.id, contact1=form.contact1.data, contact2=form.contact2.data, contact3=form.contact3.data, contact4=form.contact4.data, url=form.url.data, age=form.age.data, group=form.group.data, tagid=form.tagid.data)
    db.session.add(new_user)
    db.session.commit()

def signup_institute(form):
    new_login = Login(name=form.name.data, email=form.email.data)
    new_login.set_password(form.password.data)
    db.session.add(new_login)
    db.session.commit()
    new_user = Institution(login_id=new_login.id, scanner_id=form.scanner_id.data, kind=form.kind.data)
    db.session.add(new_user)
    db.session.commit()

def user_tag(tag_id):
    return User.query.filter_by(tagid=tag_id).first()

def instit_scan(scan_id):
    return Institution.query.filter_by(scanner_id=scan_id).first()

def delete_insit(user):
    x = Institution.query.filter_by(login_id=user).first()
    r = x.login_id
    db.session.delete(x)
    db.session.commit()
    x = Login.query.get(r)
    db.session.delete(x)
    db.session.commit()

def delete_user(user):
    x = User.query.filter_by(login_id=user).first()
    r = x.login_id
    db.session.delete(x)
    db.session.commit()
    x = Login.query.get(r)
    db.session.delete(x)
    db.session.commit()