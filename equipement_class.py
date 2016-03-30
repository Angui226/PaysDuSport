class Equipement:
    def __init__(self,json_obj):
        self.nature_libelle = json_obj['NatureLibelle']
        self.ins_nom = json_obj['InsNom']
        self.ins_numero_install = json_obj['InsNumeroInstall']
        self.equipement_id = json_obj['EquipementId']