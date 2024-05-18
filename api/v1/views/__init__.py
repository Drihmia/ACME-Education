#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.lessons import *
from api.v1.views.teachers import *
from api.v1.views.students import *
from api.v1.views.subjects import *
from api.v1.views.years import *
from api.v1.views.institutions import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.login import *
from api.v1.views.verify_email_registration import *
from api.v1.views.api_docs import *
