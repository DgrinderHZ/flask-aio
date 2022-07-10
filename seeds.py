from project import db
from project.models import BlogPost, User

# insert data
db.session.add(User(name="admin", email="admin@admin.com", password='admin'))

db.session.add(BlogPost(title="Good", description="I\'m good.", author_id=1))
db.session.add(BlogPost(title="Well", description="I\'m well.", author_id=1))
db.session.add(BlogPost(title="Excellent", description="I\'m excellent.", author_id=1))
db.session.add(BlogPost(title="Okay", description="I\'m okay.", author_id=1))

# commit the changes
try:
    db.session.commit()
except Exception:
    db.session.rollback()
finally:
    db.session.close()