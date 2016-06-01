import json
import sqlite3
from installation_class import *
from activity_equipement_class import *
from equipement_class import *
from database import *
"""
Load json and create object for the db
"""
def getJsonAndCreate():
    """
    loads three json files. Convert all json object to pyhon object and add it to the database
    """

    file_installations = open("../json_files/installations.json", "r").read()

    file_equipements = open("../json_files/equipements.json", "r").read()

    file_activites = open("../json_files/activites.json", "r").read()


    #prend en charge d un fichier json
    file_installations = json.loads(file_installations)
    file_equipements = json.loads(file_equipements)
    file_activites = json.loads(file_activites)

    #ouverture de la connecxion a la bd
    conn = sqlite3.connect('../db/database.db')
    c = conn.cursor()

    #ajout dans la bd
    for installation in file_installations['data']:
        obj_temp = Installation(installation)
        obj_temp.addDbInstallation(c)
    for equipement in file_equipements['data']:
        obj_temp = Equipement(equipement)
        obj_temp.addDbEquipement(c)
    for activite in file_activites['data']:
        obj_temp = ActivityEquipement(activite)
        obj_temp.addDbActivityEquipement(c)

    #maj/fermeture de la connexion avec la bd
    conn.commit()
    conn.close()
