# hang_man_game
It is a interesting game of guessing a leter of words , and very interesting if you guess worng letter man start hanging. 
The provided code implements a simple Hangman game in Python. It allows the user to guess letters to uncover a randomly chosen word. The game provides a visual representation of the hangman's gallows, progressing with each incorrect guess. Here is a breakdown of the code:

The code starts by importing the necessary modules: random, words, and logo.
It prints the hangman logo using logo.logo.
It selects a random word from the word_list in the words class and stores it in the variable computer_word.
The length of computer_word is stored in len_computer_word and displayed as a hint to the user.
The variable guess_word is initialized as a list of underscores representing the letters of the word to be guessed.
The main game loop starts with the variable end set to False and stage set to 6, representing the initial stage of the hangman.
Within the loop, the user is prompted to input a letter guess.
The code checks if the guessed letter is present in the computer_word, updating guess_word accordingly.
If the guess is incorrect, the code notifies the user, deducts a life (decreasing stage), and displays the corresponding hangman stage from logo.stages. If the user loses all lives (stage reaches 0), the game ends.
After each guess, the current state of guess_word is printed.
If all letters in guess_word have been correctly guessed (no underscores remain), the user wins and the game ends.
The code provides a basic implementation of the Hangman game, allowing users to interactively guess letters until they either win or lose.
