from functools import wraps
from flask import flash, redirect, session, url_for

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        
        flash('You need to login first.')
        return redirect(url_for('auth.login'))
    return wrap

