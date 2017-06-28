import os
from config import basedir
from finderscope import app
from finderscope.models import * 
import pandas as pd

def load_files():

    # load test data as single course
    course = Course(title="a_sample_course")
    db.session.add(course)
    db.session.commit()
    id_course = course.id
  
   # load person_course
    chunks = pd.read_csv('data/fake_di_data_person_course.csv', chunksize=10000)
    for chunk in chunks:
        for index, row in chunk.iterrows():
            u = User(user_id=row.user_id,
                    username=row.username,
                    ndays_act=row.ndays_act,
                    nevents=row.nevents,
                    nplay_video=row.nplay_video,
                    nchapters=row.nchapters,
                    nprogcheck=row.nprogcheck,
                    nproblem_check=row.nproblem_check,
                    nshow_answer=row.nshow_answer,
                    nvideo=row.nvideo,
                    nvideos_unique_viewed=row.nvideos_unique_viewed, 
                    nvideos_total_watched=row.nvideos_total_watched,
                    sum_dt=row.sum_dt,
                    course_id=id_course)
            db.session.add(u)
    db.session.commit() 

    # load person_course_day
    chunks = pd.read_csv('data/fake_di_data_person_course_day.csv', chunksize=10000)
    for chunk in chunks:
        for index, row in chunk.iterrows():
            ud = UserDay(
                username = row.username,
                date = row.date,
                nevents = row.nevents,
                nvideo = row.nvideo,
                nvideos_watched_sec = row.nvideos_watched_sec,
                nproblems_answered = row.nproblems_answered,
                nproblems_attempted = row.nproblems_attempted,
                sum_dt = row.sum_dt) 
            db.session.add(ud)
    db.session.commit()

if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
    db.create_all()
    load_files()
