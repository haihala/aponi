from .exceptions import AssetNotFoundException, InvalidAssetTypeException
from .dataclasses import World

from time import sleep 
from json import load
from os.path import join as pjoin   # I like to do this so it doesn't conflict with normal join.
from os.path import isdir
from os import mkdir, listdir

class Data(object):
    """
    A lazyloader to handle IO with assets and saves. Later when something like images get involved automated unloading should be implemented.
    """
    def __init__(self, root_dir):
        self.asset_dir = pjoin(root_dir, "assets")
        self.saves_dir = pjoin(root_dir, "saves")
        self.index = {"class": [], "event": [], "item": [], "mob": [], "sprite": []}
        self.check_dirs()

        self.cache = {}
        self.running = False

    def check_dirs(self):
        assert isdir(self.asset_dir), "Asset directory doesn't exist"
        if not isdir(self.saves_dir):
            # If saves directory doesn't exist assume there are no saves and just make a directory
            mkdir(self.saves_dir)
        # There should be more assumptions made of both asset dir and save dir if they exist.
        
        # Build an index
        for key in self.index:
            path = pjoin(self.asset_dir, key)
            self.index[key] = ['.'.join(i.split('.')[:-1]) for i in listdir(path)]

    def get(self, asset_id):
        if asset_id not in self.cache:
            self.load(asset_id)

        return self.cache[asset_id]

    def load(self, asset_id):
        asset_type, asset_name = asset_id.split('.')
        if asset_name not in self.index[asset_type]:
            raise AssetNotFoundException(asset_id)

        path = pjoin(self.asset_dir, asset_type, asset_name)
        asset = None
        if asset_type == "class":
            pass
        elif asset_type == "mob":
            pass
        elif asset_type == "event":
            pass        
        elif asset_type == "item":
            pass
        elif asset_type == "sprite":
            pass
        else:
            raise InvalidAssetTypeException(asset_id)
        
        self.cache[asset_id] = asset

    def save(self, world):
        # Save the world to disk
        target = pjoin(self.saves_dir, world.name)
        if not isdir(target):
            mkdir(target)
        # Put actual world to disk here.
        # Add a header of sorts with hashes for files so you don't have to write everything always.

    def get_saves(self):
        # Return list of savefiles
        return listdir(self.saves_dir)
    
    def load_save(self, world):
        target = pjoin(self.saves_dir, world)
        assert isdir(target)
        # TODO FIXME PLEASE OH LORD FUCK
        # For MVP, instead of actually loading a world, create a new one.
        return World(world)