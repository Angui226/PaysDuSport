class ActiviteEquipement:
    def __init__(self,json_obj):
        self.equipement_id=json_obj['EquipementId']
        self.libelle_activite=json_obj['ActLib']
        self.libelle_niveau=json_obj['ActNivLib']
        
    def ajoutdb_ActiviteEquipement(self,c):
        insertQuery = "INSERT INTO Activite(NumeroEquipement,LibelleActivite,LibelleNiveau) VALUES (?,?,?)"
        c.execute(insertQuery, (self.equipement_id, self.libelle_activite,self.libelle_niveau))
