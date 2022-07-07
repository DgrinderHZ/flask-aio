from app import db
from models import BlogPost  

import os
import re

def fix_uri_bug():
    uri = os.getenv("DATABASE_URL")
    print(uri) 
    # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    # rest of connection code using the connection string `uri`

fix_uri_bug()

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