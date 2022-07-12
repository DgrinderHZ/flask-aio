from project import db
from project.models import BlogPost, User

# insert data

db.session.delete(BlogPost.query.get(1))
db.session.delete(BlogPost.query.get(2))
db.session.delete(BlogPost.query.get(3))
db.session.delete(BlogPost.query.get(4))
# db.session.delete(User.query.get(1))
# commit the changes
try:
    db.session.commit()
except Exception:
    db.session.rollback()
finally:
    db.session.close()