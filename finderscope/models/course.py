from finderscope.models import db

class Course(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    users = db.relationship('User', backref='course', lazy='dynamic')

    def __init__(self,title):
        self.title = title
