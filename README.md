# Spanish Learning Game

The Spanish Learning Game is a simple flashcard-based game designed to help users learn Spanish vocabulary.
The game presents a series of Spanish words and their English translations, allowing users to practice and test their knowledge.

## Features

- Flashcard-based gameplay: The game displays a series of flashcards with Spanish words and their English translations.
- Random word selection: The game randomly selects a word from the available word list for each flashcard.
- Flip card animation: The flashcards have a flip animation to reveal the English translation of the Spanish word.
- User feedback: Users can indicate whether they know the translation of a word by clicking the "Known" or "Unknown" buttons.
- Dynamic word list: After the first run of the game, a "words_to_learn.csv" file is created to track the words that the user didn't know.
- The game will prioritize showing these words in subsequent sessions.

## How to Use

1. Run the game: Launch the Python script `main.py` to start the game.
2. Flashcard display: The game window will display a flashcard with a Spanish word on the front side.
3. Word translation: Try to recall the English translation of the displayed Spanish word.
4. Reveal translation: After a few seconds, the game will automatically flip the flashcard to reveal the English translation.
5. Feedback: Click the "Known" button if you know the translation or the "Unknown" button if you don't know it.
6. Next word: The game will automatically move to the next word and display a new flashcard after receiving feedback.
7. Word tracking: The game tracks the words that you didn't know and saves them to the "words_to_learn.csv" file for future review.
8. Review words: You can review the words you didn't know by launching the game again. The game will prioritize showing these words.

## Requirements

- Python 3.
- pandas library.
- tkinter library.

## Setup

1. Clone the repository or download the source code files.
2. Make sure you have Python 3 installed on your system.
3. Install the required libraries by running the following command: `pip install pandas`
4. Run the `main.py` script using Python: `python main.py`

The game window will open, and you can start learning Spanish vocabulary!

Enjoy learning Spanish vocabulary with the Flashcard Learning Game!
