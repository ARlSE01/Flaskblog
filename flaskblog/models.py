from flaskblog import db
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),nullable=False,unique=True)
    email=db.Column(db.String(20),nullable=False,unique=True)
    profile_pic=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(20),nullable=False)
    posts=db.relationship('Posts',backref="author",lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.id}','{self.profile_pic}')"
class Posts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(500),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)

    def __repr__(self):
        return f"Posts('{self.title}','{self.date_posted}')"