from .data import Data

from threading import Thread

class Game(object):
    """
    Main orchestrator
    """
    def __init__(self, root_dir):
        self.data = Data(root_dir)

        self.running = False
        
    def run(self):
        self.running = True
        while self.running:
            pass
