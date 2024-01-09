#!/usr/bin/env python3
"""
Module: user
Description: Keeps track of every user created.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Some Description."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
