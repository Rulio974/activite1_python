import json

class Atelier:
    def __init__(self):
        self.machine = 0
        self.dict = ""


    def load(self):
        print("Chargement des machines...")
        with open('atelier1.json') as json_data:
            data_dict = json.load(json_data)
        data_str = json.dumps(data_dict)
        self.dict = data_dict

        for key in data_dict:
            print("%s, %s"% (key, data_dict[key]))
            self.machine+=1 
        self.machine-=1 



    def save(self):
        print("Sauvegarde des machines")

    def add_t(self):
        print("Ajout d'une tache")
    
    def supr_t(self):
        print("supr d'une tache")