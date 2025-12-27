# 🃏 Blackjack Game (Python)

This is a **console-based Blackjack game** built using **Python**.  
The game follows the basic rules of Blackjack, where the goal is to get a score as close to **21** as possible without going over.

---

## 📌 Features

- Random card dealing using Python’s `random` module
- Player vs Computer gameplay
- Automatic handling of **Ace (11 → 1)** when score exceeds 21
- Computer keeps drawing cards until it reaches a safe score
- Option to **play again** after each round
- ASCII art logo support (using `art` module)

---

## 🛠️ Technologies Used

- **Python 3**
- `random` module
- Custom ASCII art from `art.py`

---

## 🎮 How the Game Works

1. The player and computer are each dealt cards.
2. Player can:
   - Type **`y`** to draw another card
   - Type **`n`** to pass
3. The computer automatically draws cards until its score is at least **16**.
4. Final scores are compared:
   - If you go above 21 → You lose
   - If the computer goes above 21 → You win
   - Otherwise, the higher score wins
5. You can choose to **play again** or exit.

---

## ▶️ How to Run the Game

1. Make sure Python is installed:
   ```bash
   python --version

## Game reference 
https://games.washingtonpost.com/games/blackjack
