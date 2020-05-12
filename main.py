import engine.game

import pathlib

def main():
    root_dir = pathlib.Path(__file__).parent.absolute()
    instance = engine.game.Game(root_dir)

    try:
        instance.run()
    except KeyboardInterrupt:
        try:
            instance.save()
        except KeyboardInterrupt:
            # Player interrupted again while saving game state.
            pass

if __name__=="__main__":
    main()