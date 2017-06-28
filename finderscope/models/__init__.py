from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

from finderscope.models.course import Course
from finderscope.models.user import User
from finderscope.models.userday import UserDay 
