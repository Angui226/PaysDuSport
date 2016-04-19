import json
import sqlite3
from installation_class import *
from activite_equipement_class import *
from equipement_class import *
from database import *

def recuperation_json():

    file_installations = open("installations.json", "r").read()
    
    file_equipements = open("equipements.json", "r").read()
    
    file_activites = open("activites.json", "r").read()

    
    #prend en charge d un fichier json
    file_installations = json.loads(file_installations)
    file_equipements = json.loads(file_equipements)
    file_activites = json.loads(file_activites)
    
    #ouverture de la connecxion a la bd
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    #ajout dans la bd
    for installation in file_installations['data']:
        obj_temp = Installation(installation)
        obj_temp.ajoutdb_Installation(c)
    for equipement in file_equipements['data']:
        obj_temp = Equipement(equipement)
        obj_temp.ajoutdb_Equipement(c)
    for activite in file_activites['data']:
        obj_temp = ActiviteEquipement(activite)
        obj_temp.ajoutdb_ActiviteEquipement(c)
    
    #maj/fermeture de la connexion avec la bd
    conn.commit()
    conn.close()