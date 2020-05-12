INTRO = "Hello."

WORLDS_HEADER = "The following saves found:"
WORLD_LINE = "\t* {}"

INVALID_TOP_COMMAND = "Command '{}' could not be found."
INVALID_SUB_COMMAND = "Parent command '{}' has no child command '{}'."
INCOMPLETE_COMMAND = "Command '{}' is missing something. Options: {}"

HELP_HEADER = "# Help\nThis is the help message. All shall be explained.\n"
EVERGREEN_HELP_HEADER = "## Evergreen\nSome commands are evergreen and always usable. Here is a list of all of them and explanations on what they do.\n"
CONTEXTUAL_HELP_HEADER = "## Contextual\nSome commands are only available in certain situations. Here is a list of all the ones currently available and what they do.\n"
COMMAND_HELP_TEMPLATE = "\t'{}': {}\n"
COMMAND_HELP_DATA = {
    "help": "Used by itself. Displays this help message.",
    "duck": "Used by itself. Quacks.",
    "quit": "Used by itself. Saves the game. When you exit with ctrl-c the game attemts to save automatically.",
    "yes": "Used by itself. Accept whatever is being prompted.",
    "no": "Used by itself. Decline whatever is being prompted.",
    "new": "Used by itself. Create a new world. The world name will be prompted.",
    "load": "Takes world name as argument. Example usage: 'load middle-earth'.",
}