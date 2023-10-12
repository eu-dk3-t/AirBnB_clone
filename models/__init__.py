#!/usr/bin/python3
"""__init__ method for models"""
from models.engine.file_storage import FileStorage


# Initialize 'FileStorage` instance
# and loads JSON file into a dict
storage = FileStorage()
storage.reload()
