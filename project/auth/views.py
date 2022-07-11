
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import login_required, login_user, logout_user
# from decorators import login_required
from .forms import LoginForm, RegisterForm
from project import db

from project.models import User

bp = Blueprint("auth", __name__, template_folder="templates")

@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and user.password == request.form['password']:
                # session['logged_in'] = True
                login_user(user)
                flash('You were logged in. Go Crazy.')
                return redirect(url_for('home.home'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(
                name=form.username.data,
                email=form.email.data,
                password=form.password.data
            )
            db.session.add(user)

            try:
                db.session.commit()
                return redirect(url_for('auth.login'))
            except Exception:
                db.session.rollback()
                flash("Email or username already exists!")
            finally:
                db.session.close()

    return render_template('register.html', form=form)



@bp.route('/logout')
@login_required
def logout():
    # session.pop('logged_in', None)
    logout_user()
    flash('You were just logged out!')
    return redirect(url_for('home.welcome'))