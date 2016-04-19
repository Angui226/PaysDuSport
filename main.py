import sqlite3
import time
from get_json_files import *
from database import *

creation_table_database()
recuperation_json()

from bottle import get, post, request, run

@get('/home') # or @route('/login')
def home():
    return '''
        <form action="/home" method="post">
            Ville: <input name="ville" type="text" />
            Sport: <input name="sport" type="text" />
            <input value="search" type="submit" />
        </form>
        '''

@post('/home') # or @route('/login', method='POST')
def do_home():
    ville = request.forms.get('ville')
    sport = request.forms.get('sport')
    
    result = select_install_ville(ville)
    return "ok"

run(host="localhost", port=8080)