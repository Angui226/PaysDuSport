import requests
import json

installation_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=json')
print ("fini")
print(installation_json_raw.json())
equipement_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J336/equipements_table/content/?format=json')
print ("fini")
activite_json_raw = requests.get('http://data.paysdelaloire.fr/api/publication/23440003400026_J334/equipements_activites_table/content/?format=json')
print ("fini")
print(activite_json_raw)


