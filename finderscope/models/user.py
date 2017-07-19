from finderscope.models import db

class User(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    user_id = db.Column(db.Integer, index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    ndays_act = db.Column(db.Integer)
    nevents = db.Column(db.Integer)
    nplay_video = db.Column(db.Integer)
    nchapters = db.Column(db.Float)
    nprogcheck = db.Column(db.Float)
    nproblem_check = db.Column(db.Float)
    nshow_answer = db.Column(db.Integer)
    nvideo = db.Column(db.Integer)
    nvideos_unique_viewed = db.Column(db.Float)
    nvideos_total_watched = db.Column(db.Float)
    sum_dt = db.Column(db.Float)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    
    def __init__(self,user_id,username,ndays_act,nevents,nplay_video,nchapters,nprogcheck,nproblem_check,nshow_answer,nvideo,nvideos_unique_viewed,nvideos_total_watched,sum_dt,course_id):
        self.user_id = user_id 
        self.username = username
        self.ndays_act = ndays_act
        self.nevents = nevents
        self.nplay_video = nplay_video
        self.nchapters = nchapters
        self.nprogcheck = nprogcheck
        self.nproblem_check = nproblem_check
        self.nshow_answer = nshow_answer
        self.nvideo = nvideo
        self.nvideos_unique_viewed = nvideos_unique_viewed
        self.nvideos_total_watched = nvideos_total_watched
        self.sum_dt = sum_dt
        self.course_id = course_id
        
    def __repr__(self):
        return '<User %r>' % (self.username)
