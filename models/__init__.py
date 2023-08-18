#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

def setup_storage():
    if getenv("HBNB_FILE_STORAGE") == 'db':
        return DBStorage()
    else:
        return FileStorage()

storage = setup_storage()
storage.reload()
