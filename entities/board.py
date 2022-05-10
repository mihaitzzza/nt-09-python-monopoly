import os
import json
from .properties import Property, Monopoly


class Board:
    def __init__(self):
        self.properties = []
        with open(os.path.join("input", "monopolies.json")) as json_file:
            data = json.load(json_file)
        for monopoly_data in data:
            monopoly = Monopoly(name=monopoly_data["monopoly"])
            for property_data in monopoly_data["properties"]:
                property_ = Property(name=property_data["name"], price=property_data["price"], rent=property_data["rent"], monopoly=monopoly)
                monopoly.add_property(property_)
                self.properties.append(property_)

