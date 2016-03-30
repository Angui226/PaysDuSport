import requests
import json


def recuperation_json():
    installations_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=json')
    equipements_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J336/equipements_table/content/?format=json')
    activites_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J334/equipements_activites_table/content/?format=json')
    
    file_installations = json.loads(installations_json_raw.text)
    file_equipements = json.loads(equipements_json_raw.text)
    file_activites = json.loads(activites_json_raw.text)
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    print("ajout installation")
    for installation in file_installations['data']:
        obj_temp = Installation(installation)
        obj_temp.ajoutdb_Installation(c)
    print("ajout equipement") 
    for equipement in file_equipements['data']:
        obj_temp = Equipement(equipement)
        obj_temp.ajoutdb_Equipement(c)
    print("ajout activité")  
    for activite in file_activites['data']:
        obj_temp = ActiviteEquipement(activite)
        obj_temp.ajoutdb_ActiviteEquipement(c)
    conn.commit()
    conn.close()