#!/usr/bin/python3
"""Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """represent an amenity.
	
	Attribute of amenity
        name (str): The name of the amenity.
    """

    name = ""
