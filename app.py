
import os
from flask import Flask, flash, redirect, render_template, request, session, url_for


from decorators import login_required
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import BlogPost
# create the database and the db table
db.create_all()


def getPosts():
    # cur = db.execute("SELECT * FROM posts;")
    # posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    # db.close()
    posts = []
    posts = BlogPost.query.all()
    return posts

def populate_db():
    # insert data
    db.session.add(BlogPost("Good", "I\'m good."))
    db.session.add(BlogPost("Well", "I\'m well."))
    db.session.add(BlogPost("Excellent", "I\'m excellent."))
    db.session.add(BlogPost("Okay", "I\'m okay."))

    # commit the changes
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
    finally:
        db.session.close()

populate_db()

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