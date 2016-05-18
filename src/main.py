#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import time
import re
import urllib


from get_json_files import *
from database import *

creation_table_database()
getJsonAndCreate()

from bottle import get, post, request, run, template, route, static_file

@route('/static/<filename>', name='static')
def server_static(filename):
    return static_file(filename, root='static')


#Home_page
@get('/') # or @route('/')
def home():
    list_activities = get_list_activites()
    list_town = get_list_town()
    return template('home', list_activities = list_activities, list_town = list_town )

@post('/') # or @route('/', method='POST')
def do_home():
    r = urllib.parse.unquote(request.body.read().decode())
    pattern = "sport="
    sport_i = r.index(pattern)
    sport = r[sport_i + len(pattern):].replace("+", " ")
    pattern2 = "&"
    pattern3 = "town="
    town_i = r.index(pattern2)
    town = r[len(pattern3) : town_i].replace("+", " ")

    #SQL injection handler
#    if not re.search("^[a-z0-9]+$", town):
#        raise InjectionSQL
#    if not re.search("^[a-z0-9]+$", sport):
#        raise InjectionSQL


    if (town != 'empty' and sport !='empty'):
        result = select_install_town(town, sport)

    elif (town != 'empty' and sport =='empty'):
        result = select_install_town_empty_sport(town)

    elif (town == 'empty' and sport !='empty'):
        result = select_install_town_empty_town(sport)
    else:
        result = select_install_town_empty_all()


    list_activities = get_list_activites()
    list_town = get_list_town()
    return template('home_requested', datas = result, list_activities = list_activities, list_town = list_town)




#Detail page
@get('/detail/<id_installation>')
def detail(id_installation):
#    if not re.search("^[a-z0-9]+$", id_installation):
#        raise InjectionSQL

    specific_installation = get_specific_installation( id_installation )
    #faire requete avec tous les equipements ayant cette installation

    return template( 'specific_installation',specific_installation  = specific_installation )

run(host="localhost", port=8080)
