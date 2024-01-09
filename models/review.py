#!/usr/bin/env python3
"""
Module: review
Description: Inherits from base model class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Some description."""
    place_id = ""
    user_id = ""
    text = ""
