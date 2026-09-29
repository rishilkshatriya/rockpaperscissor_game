# Rock Paper Scissor (GUI)

A simple Rock–Paper–Scissor game built with Python's Tkinter library. Play against the computer, keep score, and reset whenever you like.

## Features

- Start screen with a **START** button and a **QUIT** button
- Click Rock, Paper, or Scissor to play a round against the computer
- Live score tracking (Player wins, Computer wins, Draws)
- **Reset Score** button to zero the counters without restarting the program
- Fixed-size window (500x500), so the layout stays consistent

## Requirements

- Python 3
- Tkinter (comes built in with most Python installs)

No extra packages need to be installed.

## How to Run

1. Clone the Repository: git clone https://github.com/rishilkshatriya/rockpaperscissor_game.git
2. Navigate to the directory cd rockpaperscissor_game
3. Run the python program rockpaperscissor_game.py
## How It Works

- **Start screen:** A `Frame` covers the entire window when the program launches. Since it's created last in the layout, it sits on top of the game screen and blocks clicks to it. Pressing **START** calls `start_game()`, which hides this frame (`place_forget()`) and reveals the game underneath.
- **Playing a round:** Each button (Rock/Paper/Scissor) calls `play()` with the chosen option. The function picks a random choice for the computer, compares the two, updates the score counters, and refreshes the on-screen labels with `.config()`.
- **Resetting:** `reset_game()` sets all three score counters back to 0 and resets the labels to their starting text.
- **Quitting:** The **QUIT** button calls `quit_game()`, which closes the window with `window.destroy()`.

## File Structure

```
rock_paper_scissor.py   # the entire game — GUI setup, game logic, and event handlers
```

## Notes

This project was built as a learning exercise to practice:
- Tkinter widgets (`Label`, `Button`, `Frame`) and layout managers (`pack`, `grid`, `place`)
- Using `command=` with and without `lambda` for passing arguments to functions
- Updating on-screen text dynamically with `.config()`
- Layering widgets to build a simple start screen / game screen flow
