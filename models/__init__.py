#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import os


# Vérifier la valeur de la variable d'env
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    #alors importer la classe DBstorage
    from models.engine.db_storage import DBStorage
    # Créer une instance de DBStorage et la stocker dans storage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
