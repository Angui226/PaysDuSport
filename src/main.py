import sqlite3
import time
from get_json_files import *
from database import *

creation_table_database()
getJsonAndCreate()

from bottle import get, post, request, run, template

@get('/') # or @route('/login')
def home():
    return '''
        <form action="/" method="post">
            Ville: <input name="ville" type="text" />
            Sport: <input name="sport" type="text" />
            <input value="search" type="submit" />
        </form>
        '''

@post('/') # or @route('/', method='POST')
def do_home():
    town = request.forms.get('ville')
    sport = request.forms.get('sport')

    result = select_install_town(town, sport)
    return template('home', datas = result )
    
run(host="172.21.67.98", port=8080)
