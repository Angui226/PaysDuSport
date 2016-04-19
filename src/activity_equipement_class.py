class ActivityEquipement:
    def __init__(self,obj):
        """
        Create an objet ActivityEquipement
        EquipementId > primary key of the equipement
        libelle_activite > title of the practiced activity
        libelle_niveau > title of the practiced level
        """
        self.equipement_id = obj['EquipementId']
        self.libelle_activite = obj['ActLib']
        self.libelle_niveau = obj['ActNivLib']

    def addDbActivityEquipement(self,c):
        """
        Insert the object given in parametre (self) to the database given (c)
        """
        insertQuery = "INSERT INTO Activite(NumeroEquipement,LibelleActivite,LibelleNiveau) VALUES (?,?,?)"
        c.execute(insertQuery, (self.equipement_id, self.libelle_activite,self.libelle_niveau))
