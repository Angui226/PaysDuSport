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
        
    def ajoutdb_Installation(self,c):

        # print(self.numero_install)
        # print(str(self.latitude))
        # print(str(self.longitude))
        # print(self.cp)
        # print(self.commune)
        # print(self.rue)
        # print(self.train)
        # print(self.bus)
        # print(self.tram)
        # print('==========')
        if(self.rue is None):
            self.rue = ""

        insertQuery = "INSERT INTO Installation(NumeroInstall,Latitude,Longitude,CodePostal,Commune,Rue,Train,Bus,Tram) VALUES (?,?,?,?,?,?,?,?,?)"
        c.execute(insertQuery, (self.numero_install, str(self.latitude),str(self.longitude),self.cp,self.commune,self.rue,self.train,self.bus,self.tram))

            