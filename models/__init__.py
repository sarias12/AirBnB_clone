""" [init]
it's mark directories on disk as Python package directories
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
