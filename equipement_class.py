class Equipement:
    def __init__(self,json_obj):
        self.nature_libelle = json_obj['NatureLibelle']
        self.ins_nom = json_obj['InsNom']
        self.ins_numero_install = json_obj['InsNumeroInstall']
        self.equipement_id = json_obj['EquipementId']
    
    def ajoutdb_Equipement(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO Equipement VALUES ("+self.equipement_id+","+self.ins_numero_install+",'"+self.nature_libelle+"','"+self.ins_nom+"')")
        conn.commit()
        conn.close()