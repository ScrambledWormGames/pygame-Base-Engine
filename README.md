# GameEngineBase

A minimal Python game engine built with **Pygame Community Edition (pygame-ce)**, designed as a base for small 2D games.<br>
Includes a **state machine**, **entity system**, and **menu abstraction**, allowing rapid prototyping and iteration.

---

## Features

* **State management:** START, GAME, PAUSE, GAMEOVER
* **Menu support:** Start screen and pause menu with selectable options
* **Entity lifecycle:** Entities can be killed (`alive` / `kill()`), automatically removed from the game loop
* **Frame-independent movement:** `dt` (delta time) for smooth motion
* **Modular architecture:** Menus and game logic are separated
* **Safe development environment:** Always use a virtual environment to avoid polluting system Python

---

## Requirements

* Python 3.11+
* [Pygame Community Edition](https://pypi.org/project/pygame-ce/)

---

## File Structure

```
GameEngineBase/
│
├── config.py        # Window settings, FPS, and game states
├── entity.py        # Base Entity class
├── game.py          # Core game engine
├── main.py          # Entry point
├── player.py        # Player entity
├── pause.py         # Pause menu
├── start.py         # Start menu
├── requirements.txt # Dependencies
├── Makefile         # Setup and run shortcuts
```

---

## How to Run

### Using the Makefile (recommended)

```bash
make setup   # creates venv and installs dependencies
make run     # runs the game inside the venv
```

### Manual Setup (if not using Makefile)

Since the virtual environment is **not included** in the repo, you must create it manually:

```bash
python3 -m venv venv        # create virtual environment
source venv/bin/activate    # activate environment
pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

> Always run the game inside the **venv** to avoid conflicts with system Python packages.

---

## Controls

* **Start Screen:** Press **Enter** to start the game
* **Pause Menu:** Press **Escape** during gameplay

  * Navigate with **Up/Down arrows**
  * Press **Enter** to select an option:

    * Resume
    * Restart
    * Quit
* **Player Movement:** WASD keys

---

## Game Class

**`Game`**

The main engine class that orchestrates the game loop, entity updates, and state management.

**Responsibilities:**

* Initializes Pygame and sets up the window
* Maintains a **state machine** (`current_state`)
* Handles **game entities** (`update()` / `draw()`)
* Handles **input events** and menu actions
* Coordinates **menus** (`StartMenu`, `PauseMenu`)

**Core Methods:**

* `run()` — main game loop with state handling
* `get_events()` — polls events from Pygame
* `_handle_keydown(key)` — processes keyboard input according to current state
* `update()` — updates all alive entities
* `draw()` — draws all entities to the screen
* `_restart()` — resets the game entities
* `close()` — quits Pygame safely

---

## Menus

**`StartMenu`**

* Displays “Press [Enter] to start”
* Methods:

  * `update(dt)` — placeholder for future logic
  * `draw(screen)` — renders the start menu

**`PauseMenu`**

* Displays selectable options: Resume, Restart, Quit Game
* Highlights the currently selected option
* Methods:

  * `update(dt)` — handles arrow key navigation using `pygame.key.get_just_pressed()`
  * `draw(screen)` — draws overlay and menu options

---

## Entities

**`Entity`**

Base class for all game objects.

**Responsibilities:**

* `update(dt)` — update object state
* `draw(screen)` — render object
* `kill()` — mark as dead (`alive = False`)

**`Player`**

* Subclass of `Entity`
* Handles movement using **WASD keys**
* Uses delta time for smooth speed independent of frame rate
* Implements `kill()` to integrate with the entity lifecycle

---

## Entity Lifecycle

The engine uses a **killable entity pattern**:

```python
entity.kill()        # marks entity as dead
update() removes dead entities automatically
```

* Keeps the game loop clean and prevents list-modification issues
* Useful for dynamic entities like bullets or enemies

---

## Extending the Engine

**Adding entities:**

* Subclass `Entity` and implement `update()` and `draw()`

**Adding states:**

* Extend `GameState` Enum in `config.py`
* Handle new states in `Game.run()`

**Adding menu options:**

* Update `PauseMenu.options`
* Extend `_handle_keydown()` for new actions

**Restart / reset logic:**

* Use `_restart()` to reset game entities

---

## Makefile Targets

* `make setup` — create virtual environment and install dependencies
* `make run` — run the game inside the virtual environment
* `make clean` — remove `__pycache__` and the virtual environment

---

## Future Improvements

* Implement **GAMEOVER state** and menu
* Support **multiple levels** or **scenes**
* Add **submenus or settings** to PauseMenu
* Introduce **collision handling** for entities
* Add **sound and music support**

---

## AI Usage
AI usage is limited to the following items within this project.  All other elements were created by hand.

* README.md (ChatGPT)
