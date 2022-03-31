"""
AUTHOR:
"""
from .api1 import Home, FileUpload

# Registering resources in api
def initialize_routes(api):
    api.add_resource(Home, '/')
    api.add_resource(FileUpload, '/upload')
