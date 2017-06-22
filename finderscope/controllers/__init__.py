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

@app.route("/data")
@app.route("/data/<int:nopt>")
def data(nopt):
    """
    On request, this returns a list of arrays prepared from User class.

    :param nopt:
        Since I didn't manage to figure out how to make the POST request yet,
        I thought of nopt as a combination of x and y variable, that can be
        stored in a dictionary. 

    :returns data:
        A JSON string of ``count`` data points.

    """
    course = Course.query.filter_by(id=1).first()
    users = course.users
    ndata = users.count()    

    x = []
    y = []
    _id = []

    #Once we have more options, this should go into a function that will return
    #the desired arrays
    if nopt == 1:
        count = 0
        for user in users:
            if user.nevents != None and user.sum_dt != None:
                x.append(user.nevents)
                y.append(round(user.sum_dt,1))
                _id.append(user.username)
                count += 1
            else:
                pass
    """            
    elif nopt == 2:
        x = users.nvideo
        y = sum_dt
    """

    
    #x = 10 * np.random.rand(ndata) - 5
    #y = 0.5 * x + 0.5 * np.random.randn(ndata)
    A = 10. ** np.random.rand(count)
    c = np.random.rand(count)
    return json.dumps([{"_id": _id[i], "x": x[i], "y": y[i], "area": A[i],
        "color": c[i]}
        for i in range(count)])
