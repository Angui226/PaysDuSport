import sqlite3
import time
# import get_json_files
# import database

print("debut sa mère")
debut = time.time()
creation_table_database()
print ("deuxieme  paaaaaaaaartie")
recuperation_json()
fin = time.time()

print (debut-fin)