import requests
import json
from installation_class import Installation
from activite_equipement_class import ActiviteEquipement
from equipement_class import Equipement

installations_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=json')
equipements_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J336/equipements_table/content/?format=json')
activites_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J334/equipements_activites_table/content/?format=json')

file_installations = json.loads(installations_json_raw.text)
file_equipements = json.loads(equipements_json_raw.text)
file_activites = json.loads(activites_json_raw.text)


for installation in file_installations['data']:
    print(installation)

for equipement in file_equipements['data']:
    print(equipement)
    
for activite in file_activites['data']:
    print(activite)
