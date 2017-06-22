import os
from config import basedir
from finderscope import app
from finderscope.models import db, User, Course
import pandas as pd
import numpy as np


def load_files():

    course = Course(title="a_sample_course")
    db.session.add(course)
    db.session.commit()

    id_course = course.id
    #print 'course_id:', id_course

    df = pd.read_csv('data/fake_di_data_person_course.csv')
    df1 = df.set_index('user_id')

    for item in df1.index:
        #Add users 
        u = User(user_id=int(item),
                 username=df1.username[item],
                 nevents=df1.nevents[item],
                 sum_dt=df1.sum_dt[item],
                 nvideo=df1.nvideo[item],
                 course_id = id_course)
        
        db.session.add(u)
        db.session.commit()
                
    return

if __name__ == '__main__':
    #app.config['TESTING'] = True
    #app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
    db.create_all()
    
    load_files()
