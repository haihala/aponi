from .data import Data
from .static_lines import *
from .dataclasses import World

from threading import Thread
from enum import Enum, auto

class GAME_STATE(Enum):
    TRAVEL = auto()
    COMBAT = auto()
    CAMP = auto()
    YN_PROMPT = auto()

ARGLESS = "__ARGLESS__"

class Game(object):
    """
    Main orchestrator
    """
    def __init__(self, root_dir):
        self.data = Data(root_dir)
        self.world = None
        self.evergreen = {"duck": self.duck, "help": self.show_help, "quit": self.quit, "prompt": self.prompt}
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

        # if self.data.get_saves():
        #     print(WORLDS_HEADER)
        #     for world in self.data.get_saves():
        #         print(WORLD_LINE.format(world))

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

    def set_context(self, context=None, **data):
        if context == GAME_STATE.CAMP:
            pass
        elif context == GAME_STATE.COMBAT:
            pass
        elif context == GAME_STATE.TRAVEL:
            self.world.travel_destination = data["destination"]
            self.contextual = {}
        elif context == GAME_STATE.YN_PROMPT:
            self.contextual = {"yes": data["yes"], "no": data["no"]}
        else:
            assert context==None, "Unaccounted GAME_STATE: '{}'".format(context)
            # context == None
            self.contextual = {"new": self.new}
            # if self.data.get_saves():
            #     # Can only load if saves exist
            #     self.contextual["load"] = {s: lambda : self.get_world(s) for s in self.data.get_saves()}
            #     self.contextual["load"][ARGLESS] = self.get_world(self.data.get_saves()[0]) # TODO loads *some* save. debug faster with this.

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
        return "Game saved, quitting"

    def save(self): 
        # save game
        self.data.save(self.world) 
        return "Game saved"

    def prompt(self):
        if self.world:
            return self.world.prompt
        return "Game not loaded."

    def accept_quest(self, yes):
        def stump():
            self.set_context(GAME_STATE.TRAVEL, destination="Brine")

        if yes:
            def f():
                stump()
                return QUEST_ACCEPT
        else:
            def f():
                stump()
                return QUEST_DECLINE
        return f

    # Contextual
    def new(self):
        print("Name of new world:")
        name = input(">").strip() 
        self.world = World(name)
        self.set_context(GAME_STATE.YN_PROMPT, yes=self.accept_quest(True), no=self.accept_quest(False))
        self.world.prompt = QUEST_PROMPT
        return self.world.prompt
        # self.save()

    def get_world(self, name):
        self.world = self.data.load_save(name)
        self.set_context(self.world.situation)
        return self.prompt()