import sqlite3

from flask import g

def get_db(app):
    if 'db' in g:
        return g.db
    
    return sqlite3.connect(app.config['DATABASE'])

def getPosts(d):
    cur = d.execute("SELECT * FROM posts;")
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    d.close()
    return posts