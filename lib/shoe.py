#!/usr/bin/env python3

class Shoe:

    def __init__(self, brand="Unknown", size=0, material="Unknown"):
        self.brand = brand
        self.size = size
        self.material = material

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            print("brand must be a string")
            return
        if not value.strip():
            print("brand must be a non-empty string")
            return
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return
        if value <= 0:
            print("size must be greater than 0")
            return
        self._size = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if not isinstance(value, str):
            print("material must be a string")
            return
        if not value.strip():
            print("material must be a non-empty string")
            return
        self._material = value

    def wear(self):
        print(f"You put on the {self.brand} shoe. Walk comfortably!")

    def cobble(self):
        # Must match the test exactly
        print("Your shoe is as good as new!")
        self.condition = "New"
