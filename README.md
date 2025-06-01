# 🎮 Breakout Game (Pygame)

A simple **Brick Breaker (Breakout)** game built with Python and Pygame.  
This was my first hands-on game project, designed to learn the basics of 2D game development — including real-time rendering, keyboard input, collision detection, and simple physics.

![Gameplay Screenshot](images/gameplay_screenshot.png)

---

## 🚀 Project Overview

- **Goal**: Build a playable brick breaker game from scratch using Python.
- **Core Features**:
  - Paddle control using arrow keys
  - Ball bounce physics and edge detection
  - Brick grid with color-coded rows
  - Collision detection between ball, paddle, and bricks
  - Score system (+100 per brick)
  - Game over condition when the ball falls off the screen

---

## 🛠 Tech Stack

- **Language**: Python 3
- **Library**: [Pygame](https://www.pygame.org/)
- **IDE**: VS Code / Jupyter (optional)

---

## 🎯 Gameplay Highlights

* Smooth paddle movement using `pygame.key.get_pressed()`
* Clean separation of rendering and logic
* Accurate brick collision handling using `pygame.Rect`
* Simple scoring system displayed in real time

---

## 💬 Lessons Learned

* Handling real-time input with keyboard states
* Using tuples to associate color data with Rects (since `pygame.Rect` is immutable)
* Structuring a game loop (input → update → draw → repeat)
* Managing FPS to balance speed and playability
