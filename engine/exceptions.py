from dataclasses import dataclass
"""
Code errors
"""

class AssetException(Exception):
    """
    Generic exception with assets
    """
    pass

class InvalidAssetTypeException(AssetException):
    """
    For when the cache handler tries to load something but the type presented doesn't exist.
    """
    pass

class AssetNotFoundException(AssetException):
    """
    For when the cache handler tries to load something but an asset with the specified name doesn't exist.
    """
    pass


class MissingGameStateException(Exception):
    """
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, state):
        self.message = "Unaccounted GAME_STATE: '{}'".format(state)
"""
User errors
"""

@dataclass
class InputException(Exception):
    """
    Generic exception with the user input
    Attributes:
        message -- explanation of the error
    """
    message: str        

class TopCommandException(InputException):
    """
    Invalid top level command
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, command):
        self.message = "Command '{}' could not be found.".format(message)

class SubCommandException(InputException):
    """
    Correct top level command, invalid subcommand
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, parent, child):
        self.message = "Parent command '{}' has no child command '{}'.".format(parent, child)

class IncompleteCommandException(InputException):
    """
    Correct top level command, requires subcommand that wasn't provided.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, parent, options):
        self.message = "Command '{}' is missing something. Options: {}".format(parent, options)
