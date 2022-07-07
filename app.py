
import os
from flask import Flask, flash, redirect, render_template, request, session, url_for


from decorators import login_required
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import BlogPost
# create the database and the db table
import os
import re

uri = os.getenv("DATABASE_URL")
print("[INFO]", uri) 
# or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)


db.create_all()


def getPosts():
    # cur = db.execute("SELECT * FROM posts;")
    # posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    # db.close()
    posts = []
    posts = BlogPost.query.all()
    return posts


@app.route('/')
@login_required
def home():
    posts = getPosts()
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