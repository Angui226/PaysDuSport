#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import time
import re
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
    town = request.forms.get('town')
    sport = request.forms.get('sport')
    #sport = unicode (sport, "utf-8")

    #SQL injection handler
#    if not re.search("^[a-z0-9]+$", town):
#        raise InjectionSQL
#    if not re.search("^[a-z0-9]+$", sport):
#        raise InjectionSQL

    print (town)

    print (sport)

    if (town != 'empty' and sport !='empty'):
        print ("1")
        result = select_install_town(town, sport)

    elif (town != 'empty' and sport =='empty'):
        print ("2")
        result = select_install_town_empty_sport(town)

    elif (town == 'empty' and sport !='empty'):
        print ("3")
        result = select_install_town_empty_town(sport)

    #if (town == 'empty'and sport =='empty'):


    list_activities = get_list_activites()
    list_town = get_list_town()
    return template('home_requested', datas = result, list_activities = list_activities, list_town = list_town)

run(host="localhost", port=8080)
