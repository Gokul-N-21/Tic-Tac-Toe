# Tic-Tac-Toe 👾

## Project Overview
  This project is a Python-based implementation of the classic **Tic-Tac-Toe** game. It is designed as an evolutionary coding project, transitioning from a basic local multiplayer game to a sophisticated version featuring an intelligent AI opponent. The project demonstrates how to build game logic from the ground up, handle user input validation, and implement decision-making algorithms for a computer-controlled player.

---

## Implementation and Use Cases

### Implementation
The project was developed in three distinct phases:

  * **Phase 1 (PvP)**: Established the core game engine, including the board display, win-condition checking (rows, columns, and diagonals), and turn-based logic for two human players.
  * **Phase 2 (Random AI)**: Introduced a computer opponent that utilizes a basic `random` selection algorithm to choose from available spaces on the board.
  * **Phase 3 (Smart AI)**: Upgraded the computer's intelligence. The AI now scans the board for immediate winning opportunities or defensive moves to block the human player before falling back to a random move.

### Use Cases

  * **Local Multiplayer**: Play against a friend on the same machine.
  * **Single Player (Easy)**: Practice against a randomized AI (Phase 2).
  * **Single Player (Hard)**: Challenge a strategic AI that actively prevents you from winning (Phase 3).

---

## Libraries Used and Their Purposes

  * **`random` (Standard Library)**:
    * `random.randint`: Used at the start of the game to fairly decide which player (Human or Computer) takes the first turn.
    * `random.choice`: Used by the AI to select a move from a list of available board positions.

---

## Requirements
To run this project, you need:

  * Python 3.x installed on your system.
  * A terminal or command prompt to execute the script.
  * No external third-party packages are required (uses Python Standard Library only).

---

## Learning Outcomes
By developing this project, the following concepts were mastered:

  * **Data Structures**: Using `lists` to represent and update a 3x3 game board.
  * **Game Loop Logic**: Managing "Game On" states and handling replayability via nested `while` loops.
  * **Input Validation**: Implementing `try/except` blocks and conditional checks to handle invalid user inputs (non-integers or occupied spaces).
  * **Algorithmic Thinking**: Developing a prioritized "Look-Ahead" logic for the AI to simulate basic strategic decision-making.
  * **Code Refactoring**: Building modular functions (like `win_check` and `space_check`) that can be reused across different versions of the game.
