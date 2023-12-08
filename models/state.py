#!/usr/bin/python3
"""This module defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

    Attributes of state:
        name (str): The name of the state.
    """

    name = ""
