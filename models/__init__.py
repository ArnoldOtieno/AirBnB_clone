#!/usr/bin/python3
"""model init file"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
