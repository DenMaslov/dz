import yaml

from config import Config
from soldier import Soldier
from vehicle import Vehicle
from squad import Squad
from army import Army

class Reader:

    def __init__(self) -> None:
        self.__data = {}
        self.__res_armies = []
        self.__start_from_step = 0

    def read(self, name: str) -> list:
        """Reads data and starts parsing"""
        with open(name, 'r') as file:
            try:
                self.__data = yaml.load(file)
            except yaml.YAMLError as exc:
                print(exc)
        return self.parse()

    def create_soldier(self, data) -> Soldier:
        """Return obj of solider"""
        soldier = Soldier()
        soldier.health = data["health"]
        soldier.experience = data["experience"]
        return soldier

    def create_vehicle(self, data) -> Vehicle:
        """Return obj of vehicle"""
        vehicle = Vehicle()
        for i in range(data["operators"]):
            vehicle.add_operator(Soldier())
        return vehicle

    @property
    def start_from_step(self) -> int:
        """Returns start step"""
        return self.__start_from_step
    
    @start_from_step.setter
    def start_from_step(self, step: int) -> None:
        if isinstance(step, int):
            self.__start_from_step = step
        else:
            raise ValueError("Step must be int")

    def parse(self) -> list:
        """Retrieves components from data"""
        seed = self.__data["SEED"]
        Config.seed = seed
        self.start_from_step = self.__data["STEP"]
        data = self.__data["ARMIES"]
        armies = []
        
        for key in data:
            armies.append(data[key])
        
        return self.parse_army(armies=armies)

    def parse_army(self, armies: list) -> list:
        """Returns list of armies"""
        data_armies = []
        for i in range(len(armies)):
            squads = []
            for j in range(len(armies[i])):
                squads.append(armies[i][j])
            data_armies.append(squads)
        res_armies = []
        temp = 0
        for army in data_armies:
            for army_element in army:
                for key in army_element:
                    s = Squad()
                    if key == "name":
                        res_armies.append(Army(name=army_element[key]))
                    else:
                        for unit in army_element[key]:
                            for key in unit:
                                if key == "Vehicle":
                                    s.add_unit(self.create_vehicle(unit[key]))
                                if key == "Solider":
                                    s.add_unit(self.create_soldier(unit[key]))
                        res_armies[temp].add_squad(s)
            temp += 1
        return res_armies


                
    


                        

        