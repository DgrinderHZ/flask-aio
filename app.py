
import os
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
from db import get_db, getPosts


from decorators import login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['DATABASE'] = 'sample.db'



@app.route('/')
@login_required
def home():
    posts = []
    try:
        d = get_db(app)
        posts = getPosts(d)
    except sqlite3.OperationalError:
        flash('Missing the DB!')
    return render_template('index.html', posts=posts)

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials.'
            return render_template('login.html', error=error)
        
        session['logged_in'] = True
        flash('You were just logged in!')
        return redirect(url_for('home'))
    
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('home'))



# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == '__main__':
    app.run(debug=True)