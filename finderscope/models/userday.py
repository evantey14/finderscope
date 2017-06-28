from finderscope.models import db

class UserDay(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    date = db.Column(db.String)
    user_id = db.Column(db.Integer, index=True)
    username = db.Column(db.String(64), index=True)
    nevents = db.Column(db.Integer)
    nvideos = db.Column(db.Integer)
    nvideos_watched_sec = db.Column(db.Float)
    nproblems_answered = db.Column(db.Integer)
    nproblems_attempted = db.Column(db.Integer)
    sum_dt = db.Column(db.Float)
    total_time_5 = db.Column(db.Float)
    total_video_time_5 = db.Column(db.Float)
    total_problem_time_5 = db.Column(db.Float)
    total_text_time_5 = db.Column(db.Float)


    def __init__(self,username,date,nevents,nvideo,nvideos_watched_sec,nproblems_answered,nproblems_attempted,sum_dt
):
        self.username = username
        self.date = date
	self.nevents = nevents
        self.nvideo = nvideo
       	self.nvideos_watched_sec = nvideos_watched_sec
	self.nproblems_answered = nproblems_answered
	self.nproblems_attempted = nproblems_attempted
        self.sum_dt = sum_dt
