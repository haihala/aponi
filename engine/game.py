from .data import Data
from .static_lines import *
from .dataclasses import World
from .dataclasses.world import GAME_STATE

from threading import Thread

ARGLESS = "__ARGLESS__"

class Game(object):
    """
    Main orchestrator
    """
    def __init__(self, root_dir):
        self.data = Data(root_dir)
        self.world = None
        self.evergreen = {"duck": self.duck, "help": self.show_help, "quit": self.quit}
        self.set_context()

        self.running = False

    @property
    def options(self):
        ret = {}
        ret.update(self.evergreen)
        ret.update(self.contextual)
        return ret

    def run(self):
        self.running = True
        # Repl
        print(INTRO)
        print(self.show_help())

        if self.data.get_saves():
            print(WORLDS_HEADER)
            for world in self.data.get_saves():
                print(WORLD_LINE.format(world))

        while self.running:
            cmd = input('> ').strip().split()
            func, error_message = self.find_function(cmd)
            if error_message == None:
                print(func())
            else:
                print(error_message)

    def find_function(self, cmd, stub=None, parent=None):
        if stub == None:
            stub = self.options

        if cmd[0] not in stub:
            if parent:
                # Issue with subcommand
                return (None, INVALID_SUB_COMMAND.format(parent, cmd[0]))
            else:
                # Issue with root command
                return (None, INVALID_TOP_COMMAND.format(cmd[0]))
        else:
            if type(stub[cmd[0]]) is dict:
                if len(cmd) > 1:
                    return self.find_function(cmd[1:], stub=stub[cmd[0]], parent=cmd[0])
                else:
                    if ARGLESS in stub:
                        return (stub[ARGLESS], None)
                    else:
                        return (None, INCOMPLETE_COMMAND.format(parent, ', '.join(["'{}'".format(i) for i in stub.keys()])))
            else:
                return (stub[cmd[0]], None)

    def set_context(self, context=None):
        if context == GAME_STATE.CAMP:
            pass
        elif context == GAME_STATE.COMBAT:
            pass
        elif context == GAME_STATE.SOCIAL:
            pass
        elif context == GAME_STATE.TRAVEL:
            pass
        else:
            assert context==None, "Unaccounted GAME_STATE: '{}'".format(context)
            # context == None
            self.contextual = {"new": self.new}
            if self.data.get_saves():
                # Can only load if saves exist
                self.contextual["load"] = {s: lambda : self.get_world(s) for s in self.data.get_saves()}

    # Evergreen
    def duck(self):
        return "quack"

    def show_help(self):
        collector = ""
        collector += HELP_HEADER
        collector += '\n'+EVERGREEN_HELP_HEADER
        for cmd in self.evergreen:
            collector += COMMAND_HELP_TEMPLATE.format(cmd, COMMAND_HELP_DATA[cmd])

        collector += '\n'+CONTEXTUAL_HELP_HEADER
        for cmd in self.contextual:
            collector += COMMAND_HELP_TEMPLATE.format(cmd, COMMAND_HELP_DATA[cmd])
            
        return collector

    def quit(self):
        self.save()
        self.running = False

    def save(self): 
        # save game
        self.data.save(self.world) 

    # Contextual
    def new(self):
        print("Name of new world:")
        name = input(">").strip() 
        self.world = World(name)
        self.save()

    def get_world(self, name):
        self.world = self.data.load_save(name)
        self.set_context(self.world.situation)