import sqlite3
import time
from get_json_files import *
from database import *

creation_table_database()
getJsonAndCreate()

from bottle import get, post, request, run, template

@get('/') # or @route('/login')
def home():
    list_activities = get_list_activites()
    list_town = get_list_town()
    return template('home', list_activities = list_activities, list_town = list_town )

@post('/') # or @route('/', method='POST')
def do_home():
    town = request.forms.get('ville')
    sport = request.forms.get('sport')

    result = select_install_town(town, sport)
    list_activities = get_list_activites()
    list_town = get_list_town()
    return template('home_requested', datas = result, list_activities = list_activities, list_town = list_town)

run(host="localhost", port=8080)
