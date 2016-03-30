class Equipement:
    def __init__(self,json_obj):
        self.nature_libelle = json_obj['NatureLibelle']
        self.ins_nom = json_obj['InsNom']
        self.ins_numero_install = json_obj['InsNumeroInstall']
        self.equipement_id = json_obj['EquipementId']
    
    def ajoutdb_Equipement(self,c):

        insertQuery = "INSERT INTO Equipement(NumeroEquipement,NumeroInstallation,NatureLibelle,InsNom) VALUES (?,?,?,?)"
        c.execute(insertQuery, (self.equipement_id, self.ins_numero_install,self.nature_libelle,self.ins_nom))
