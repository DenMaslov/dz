import yaml

from soldier import Soldier
from vehicle import Vehicle
from squad import Squad
from army import Army

class Reader:

    def __init__(self) -> None:
        self.__data = {}
        self.__res_armies = []

    def read(self, name: str) -> list:
        with open( name, 'r') as file:
            try:
                self.__data = yaml.load(file)
            except yaml.YAMLError as exc:
                print(exc)
        return self.parser()

    def create_soldier(self, data):
        soldier = Soldier()
        soldier.health = data["health"]
        soldier.experience = data["experience"]
        return soldier

    def create_vehicle(self, data):
        vehicle = Vehicle()
        for i in range(data["operators"]):
            vehicle.add_operator(Soldier())
        return vehicle

    def parser(self):
        data = self.__data["ARMIES"]
        armies = []
        
        for key in data:
            armies.append(data[key])
        
        return self.army_parser(armies=armies)

    def army_parser(self, armies: list) -> list:
        data_armies = []
        for i in range(len(armies)):
            squads = []
            for j in range(len(armies[i])):
                squads.append(armies[i][j])
            data_armies.append(squads)
        res_armies = []
        temp = 0
        for army in data_armies:
            for el in army:
                for key in el:
                    s = Squad()
                    if key == "name":
                        res_armies.append(Army(name=el[key]))
                    else:
                        for unit in el[key]:
                            for key in unit:
                                if key == "Vehicle":
                                    s.add_unit(self.create_vehicle(unit[key]))
                                if key == "Solider":
                                    s.add_unit(self.create_soldier(unit[key]))
                        res_armies[temp].add_squad(s)
            temp += 1
        return res_armies


                
    


                        

        