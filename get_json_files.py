import requests
import json


def recuperation_json():
    installations_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=json')
    equipements_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J336/equipements_table/content/?format=json')
    activites_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J334/equipements_activites_table/content/?format=json')
    
    #prend en charge d un fichier json
    file_installations = json.loads(installations_json_raw.text)
    file_equipements = json.loads(equipements_json_raw.text)
    file_activites = json.loads(activites_json_raw.text)
    
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