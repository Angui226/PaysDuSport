#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main function. Receive requests, return template and data from the database
"""
import sqlite3 #Database management system
import time
import urllib #recuperer corps requete http
import json #permet de traiter du json
from get_json_files import *
from database import *

creation_table_database()
get_json_and_create()

from bottle import get, post, request, run, template, route, static_file,response


@route('/static/<filename>', name='static')
def server_static(filename):
    """
    function that redirect all files (css and js) to the directory static
    """
    return static_file(filename, root='static')


#Home_page
@get('/') # or @route('/')
def home():
    """
    return the home page with the list of the activities and the towns in the db
    """
    list_activities = get_list_activites()
    list_town = get_list_town()
    return template('home', list_activities = list_activities, list_town = list_town )

@post('/') # or @route('/', method='POST')
def do_home():
    """
    return a template with the list of the request (town and sport given by the user)
    """
    r = urllib.parse.unquote(request.body.read().decode())
    r = r.replace("+", " ")

    r = r.split("&")
    tab1 = r[0].split("=")
    tab2 = r[1].split("=")

    if (tab1[0] == "town"):
        town = tab1[1]
        sport =tab2[1]
    else :
        sport =tab1[1]
        town = tab2[1]


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



@post('/change') # or @route('/', method='POST')
def do_change_town():
    """
    refresh the list of the sport according to the selected town
    """
    r = urllib.parse.unquote(request.body.read().decode())
    pattern = "town="
    town_i = r.index(pattern)
    town = r[town_i + len(pattern):].replace("+", " ")

    list_activities = get_list_activites_changed(town)
    json_response = json.dumps(list_activities)
    response.content_type = 'application/json; charset=UTF-8 '
    return json_response



#Detail page
@get('/detail/<id_installation>')
def detail(id_installation):
    """
    return all the detail of an installation with its id as argument
    """
    specific_installation = get_specific_installation( id_installation )
    #faire requete avec tous les equipements ayant cette installation

    return template( 'specific_installation',specific_installation  = specific_installation )

run(host="localhost", port=8080)
