from abc import ABC,abstractclassmethod

class car(ABC):
    def __init__(self,brand, model, year):
        self.brand= brand
        self.model=model
        self.year=year
        self.engine_started= True
    def Startengine(self):
        if not self.engine_started:
            print(f"Starting  the {self.model}'s  engine")
            self.engine_started= True
        else:
            print('engine is already  running')
            