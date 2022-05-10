import os
import json
from entities.properties import Property, Monopoly
from entities.spaces import TaxSpace, CornerSpace, PropertySpace

PREDEFINED_SPACES = {
    0: CornerSpace(0, is_start=True),
    10: CornerSpace(10, is_free_parking=True),
    20: CornerSpace(20, is_visit_jail=True),
    30: CornerSpace(30, is_go_to_jail=True),
    2: TaxSpace(2),
    4: TaxSpace(4),
    6: TaxSpace(6),
    12: TaxSpace(12),
    15: TaxSpace(15),
    19: TaxSpace(19),
    22: TaxSpace(22),
    25: TaxSpace(25),
    28: TaxSpace(28),
    31: TaxSpace(31),
    33: TaxSpace(33),
    35: TaxSpace(35),
    37: TaxSpace(37),
    38: TaxSpace(38),
    39: TaxSpace(39)
}

class Board:
    def __init__(self):
        self.properties = []
        self.spaces = []

        with open(os.path.join("input", "monopolies.json")) as json_file:
            data = json.load(json_file)

        for monopoly_data in data:
            monopoly = Monopoly(name=monopoly_data["monopoly"])
            for property_data in monopoly_data["properties"]:
                property_ = Property(name=property_data["name"], price=property_data["price"], rent=property_data["rent"], monopoly=monopoly)
                monopoly.add_property(property_)
                self.properties.append(property_)

        next_property_index = 0

        for index in range(0, 40):
            if index in PREDEFINED_SPACES:
                self.spaces.append(PREDEFINED_SPACES[index])
            else:
                property_space = PropertySpace(index, self.properties[next_property_index])
                self.spaces.append(property_space)
                next_property_index += 1
        print(self.spaces)




