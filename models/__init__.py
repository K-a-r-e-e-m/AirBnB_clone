#!/usr/bin/python3
"""This file contain initialization code for the Package,
such as importing submodules, defining variables,
or executing other code.
"""

from models.engine.file_storage import FileStorage


# initialize instance or execute code when a models package is imported
storage = FileStorage()
storage.reload()
