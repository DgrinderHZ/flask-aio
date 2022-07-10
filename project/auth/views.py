
from flask import Blueprint, redirect, render_template, request, session, url_for, flash
from decorators import login_required

from project.models import User

bp = Blueprint("auth", __name__, template_folder="templates")

@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(name=request.form['username']).first()
        if user is None or user.password != request.form['password']:
            error = 'Invalid Credentials.'
            return render_template('login.html', error=error)
        
        session['logged_in'] = True
        flash('You were just logged in!')
        return redirect(url_for('home.home'))
    
    return render_template('login.html')


@bp.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('home.welcome'))