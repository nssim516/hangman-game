# Hangman

A fun and interactive Hangman game built using Python. Try to guess the word before the stick figure is fully drawn!

## Features

- Randomly selects a word from a predefined list.
- Interactive text-based gameplay.
- Visual representation of the hangman with each wrong guess.
- Tracks incorrect guesses and displays used letters.

## How to Play

1. Clone the repository:
`git clone https://github.com/yourusername/hangman.git`

2. Run the Python script:
`python hangman.py`

3. Guess one letter at a time by typing it in the console.
4. Correct guesses will reveal the letters in the word.
5. Wrong guesses will add parts to the hangman. You lose after 6 incorrect guesses.
   
## Example Gameplay
```
Welcome to Hangman!
_ _ _ _ _ _ 
Guess a letter: o
Correct!
_ o _ _ o _ 
Guess a letter: p
Wrong!
  +---+
  O   |
      |
      |
      |
=========
Letters used: p
```

