"""
The entrypoint to the game.
"""
from game import Game


def main():
    """
    Entrypoint function for the application
    """
    try:
        this = Game()
        this.run()
    except Exception as e:
        print(f"There was an issue with the game: {e}\n", e)
        raise e
    finally:
        this.close()


if __name__ == "__main__":
    main()
