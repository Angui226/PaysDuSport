#!/usr/bin/env python3

class Installation:
    def __init__(self,obj):
        self.nom = obj['geo']['name']
        self.latitude=obj['Latitude']
        self.longitude=obj['Longitude']
        self.numero_install=obj['InsNumeroInstall']
        self.cp=obj['InsCodePostal']
        self.commune=obj['ComLib']
        self.rue=obj['InsLibelleVoie']
        self.train=obj['InsTransportTrain']
        self.bus=obj['InsTransportBus']
        self.tram=obj['InsTransportTram']

    def addDbInstallation(self,c):
        if(self.rue is None): #permet de catcher le cas ou il n y a pas de rue entree
            self.rue = ""

        insertQuery = "INSERT INTO Installation(NumeroInstall,Nom,Latitude,Longitude,CodePostal,Commune,Rue,Train,Bus,Tram) VALUES (?,?,?,?,?,?,?,?,?,?)"
        c.execute(insertQuery, (self.numero_install,self.nom,str(self.latitude),str(self.longitude),self.cp,self.commune,self.rue,self.train,self.bus,self.tram))
