import sqlite3
import time
# import get_json_files
# import database

debut = time.time()
creation_table_database()
recuperation_json()
fin = time.time()

print (debut, fin)