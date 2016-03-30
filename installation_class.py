#!/usr/bin/env python3

class Installation:
    def __init__(self,json_obj):
        self.latitude=json_obj['Latitude']
        self.longitude=json_obj['Longitude']
        self.numero_install=json_obj['InsNumeroInstall']
        self.cp=json_obj['InsCodePostal']
        self.commune=json_obj['ComLib']
        self.rue=json_obj['InsLibelleVoie']
        self.train=json_obj['InsTransportTrain']
        self.bus=json_obj['InsTransportBus']
        self.tram=json_obj['InsTransportTram']
        
    def ajoutdb_installation():
        