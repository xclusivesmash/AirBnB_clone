#!/usr/bin/env python3
"""
Module: __init__
Description: initialization file.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
