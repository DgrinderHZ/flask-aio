

from flask import Flask, flash, redirect, render_template, request, session, url_for

from functools import wraps

from decorators import login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'



@app.route('/')
@login_required
def home():
    return render_template('index.html')

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
        return redirect(url_for('welcome'))
    
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)