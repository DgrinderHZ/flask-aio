from flask import Blueprint, render_template

from decorators import login_required
from project.models import BlogPost

bp = Blueprint("home", __name__, template_folder='templates')

def getPosts():
    # cur = db.execute("SELECT * FROM posts;")
    # posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    # db.close()
    posts = []
    posts = BlogPost.query.all()
    return posts


@bp.route('/')
@login_required
def home():
    posts = getPosts()
    return render_template('index.html', posts=posts)

@bp.route('/welcome')
def welcome():
    return render_template('welcome.html')