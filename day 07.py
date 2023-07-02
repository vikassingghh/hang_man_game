# create a hangman game
#first importing a random class
import random
# importing a class words which i create to store words 
import words
# importing logo in which i create a logo of a hangman
import logo
# start with printing logo 
print(logo.logo)
# i create a variable which store random words from words class in which word_list
computer_word = random.choice(words.word_list)
# create a variable which store the length of computer_word
len_computer_word = len(computer_word)
# give a hint to user that computer choose a word of len_computer_word
print(f"Computer chossen word of {len_computer_word} letters.")
# crate a list of "_" according to computer word 
guess_word = []
for i in range(len_computer_word):
    guess_word.append("_")
print(guess_word)
# create a variable of boolen
end = False
# we have a 6 stages of hangman and create a variable that store it
stage = 6

while not end:
    # variable that store our guess word
    guess = input("Guess your letter:").lower()
    # create a loop that check the guess letter in the computer word or not.
    for j in range(0,len_computer_word):
        letter=computer_word[j]
        if letter==guess:
            guess_word[j]=guess
    if guess not in computer_word:
      print(f"you guessed {guess} letter which is not in word try other letter.\n you lose a life.")
      stage = stage-1
      print(logo.stages[stage])
      if stage==0:
        end=True
        print("You loose.")
            
    print(guess_word)
    
    if "_" not in guess_word:
        end = True
        print("You win.")
 













   