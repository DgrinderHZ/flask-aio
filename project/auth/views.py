
from flask import Blueprint, redirect, render_template, request, session, url_for, flash
from decorators import login_required
from .forms import LoginForm

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
                session['logged_in'] = True
                flash('You were logged in. Go Crazy.')
                return redirect(url_for('home.home'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)



@bp.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('home.welcome'))