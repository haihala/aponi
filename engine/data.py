from .exceptions import AssetNotFoundException, InvalidAssetTypeException

from time import sleep 
from json import load
from os.path import join as pjoin   # I like to do this so it doesn't conflict with normal join.
from os.path import isdir
from os import mkdir

class Data(object):
    """
    A lazyloader to handle IO with assets and saves. Later when something like images get involved automated unloading should be implemented.
    """
    def __init__(self, root_dir):
        self.asset_dir = pjoin(root_dir, "assets")
        self.saves_dir = pjoin(root_dir, "saves")
        self.check_dirs()

        self.cache = {}
        self.running = False

    def check_dirs(self):
        assert isdir(self.asset_dir), "Asset directory doesn't exist"
        if not isdir(self.saves_dir):
            # If saves directory doesn't exist assume there are no saves and just make a directory
            mkdir(self.saves_dir)
        # There should be more assumptions made of both asset dir and save dir if they exist.


    def get(self, asset_id):
        if asset_id not in self.cache:
            self.load(asset_id)

        return self.cache[asset_id]

    def load(self, asset_id):
        asset_type, asset_name = asset_id.split('.')

        asset = None
        if asset_type == "class":
            pass
        elif asset_type == "mob":
            pass
        elif asset_type == "event":
            pass        
        elif asset_type == "item":
            pass
        elif asset_type == "save":
            pass
        else:
            raise InvalidAssetTypeException(asset_id)
        
        if asset == None:
            raise AssetNotFoundException(asset_id)

        self.cache[asset_id] = asset