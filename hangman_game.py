import random
import hangmanStages
import random
from words import word_list

lives=6
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for letter in range(len(chosen_word)):
    display= display+["_"]
print (display)
game_over=False
while not game_over:
    guessed_letter = input("guess a letter: ").lower()
    for position in range(len(chosen_word)) :
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives = lives-1
        if lives ==0 :
            game_over=True
            print("you lose !!")
    if '_' not in display:
        game_over=True
        print ("you win !!")
    print(hangmanStages.hangmanstages[lives])