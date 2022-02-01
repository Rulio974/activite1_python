import json

class Atelier:
    def __init__(self):
        self.machine = 0

    def load(self):
        with open('atelier1.json') as json_data:
            data_dict = json.load(json_data)
        data_str = json.dumps(data_dict)
        print(data_dict)

        print("Chargement des machines")

    def save(self):
        print("Sauvegarde des machines")

    def add_t(self):
        print("Ajout d'une tache")
    
    def supr_t(self):
        print("supr d'une tache")