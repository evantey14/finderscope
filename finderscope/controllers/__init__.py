from flask import render_template, flash, redirect, session, url_for, request, g, json, jsonify, send_from_directory
from finderscope import app, db
import numpy as np
from finderscope.models import User, Course

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    When you request the root path, you'll get the index.html template.
    """

    #Get the course and user info and pass on to index
    course = Course.query.filter_by(id=1).first()
    users = course.users

    return render_template("index.html",
                           course = course)

@app.route("/data/", methods=['POST'])
def data():
    data = json.loads(request.data)
    
    course = Course.query.filter_by(id=1).first()
    users = course.users
    ndata = users.count()    

    x = []
    y = []
    _id = []

    #Once we have more options, this should go into a function that will return
    #the desired arrays
    count = 0
    for user in users:
        if user.__dict__[data['x']] != None and user.__dict__[data['y']] != None:
            x.append(user.__dict__[data['x']])
            y.append(round(user.__dict__[data['y']],1))
            _id.append(user.username)
            count += 1
        else:
            pass
    
    #x = 10 * np.random.rand(ndata) - 5
    #y = 0.5 * x + 0.5 * np.random.randn(ndata)
    A = 10. ** np.random.rand(count)
    c = np.random.rand(count)
    return json.dumps([{"_id": _id[i], "x": x[i], "y": y[i], "area": A[i],
        "color": c[i]}
        for i in range(count)])

@app.route("/getpoint/", methods=['POST'])
def getpoint():
    point = json.loads(request.data)
    user = User.query.filter(User.username == point['_id']).first()
    if user is None:
        return json.dumps({'status':'failed'})
    else:
        user_dict = user.__dict__
        user_dict.pop('_sa_instance_state', None) # sqlalchemy instance cannot be serialized so remove it
        return json.dumps({'status':'success', 'user':user_dict})
