class ActiviteEquipement:
    def __init__(self,json_obj):
        self.equipement_id=json_obj['EquipementId']
        self.libelle_activite=json_obj['ActLib']
        self.libelle_niveau=json_obj['ActNivLib']