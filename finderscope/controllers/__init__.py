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
    course = Course.query.filter_by(id=1).first()
    return render_template("index.html", course = course)

@app.route("/plot/person_course", methods=['POST'])
def plot_person_course():
    req_data = json.loads(request.data)
    x_axis = req_data['x']
    y_axis = req_data['y']

    course = Course.query.filter_by(id=1).first()
    users = course.users
    count = users.count()

    _id = []
    x = []
    y = []
    area = 10. ** np.random.rand(count)
    color = np.random.rand(count)

    for user in users:
        user_dict = user.__dict__
        print(user_dict)
        if user_dict[x_axis] is not None and user_dict[y_axis] is not None:
            _id.append(user_dict['username'])
            x.append(user_dict[x_axis])
            y.append(round(user_dict[y_axis],1))

    return json.dumps([{
        "_id": _id[i], 
        "x": x[i], 
        "y": y[i], 
        "area": area[i], 
        "color": color[i]} for i in range(len(x))])

@app.route("/getpoint", methods=['POST'])
def getpoint():
    point = json.loads(request.data)
    user = User.query.filter(User.username == point['_id']).first()
    if user is None:
        return json.dumps({'status':'failed'})
    else:
        user_dict = user.__dict__
        user_dict.pop('_sa_instance_state', None) # sqlalchemy instance cannot be serialized so remove it
        return json.dumps({'status':'success', 'user':user_dict})
