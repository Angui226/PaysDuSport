"""
Class Equipement
"""
class Equipement:
    def __init__(self,obj):
        """
        Create an objet Equipement
        nature_libelle > nature of the equipement
        ins_nom > name of the equipement
        ins_numero_install > foreign key of the installation
        equipement_id > primary key of the equipement
        """
        self.nature_libelle = obj['NatureLibelle']
        self.ins_nom = obj['InsNom']
        self.ins_numero_install = obj['InsNumeroInstall']
        self.equipement_id = obj['EquipementId']


    def add_db_equipement(self,c):
        """
        Insert the object given in parametre (self) to the database given (c)
        """
        insertQuery = "INSERT INTO Equipement(NumeroEquipement,NumeroInstallation,NatureLibelle,InsNom) VALUES (?,?,?,?)"

        c.execute(insertQuery, (self.equipement_id,self.ins_numero_install,self.nature_libelle,self.ins_nom))
