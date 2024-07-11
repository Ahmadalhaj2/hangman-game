import random
import stages_hangman
import words
#have to package to import words and stages in game
print(stages_hangman.logo)
#this line choise random word to guess it
chosen_word = random.choice(words.word_list)
number_of_letters = len(chosen_word)

letters_list = []
for letter in chosen_word:
    letters_list.append("_")

print(f"Number of letters in the word = {number_of_letters}")
print(f"{' '.join(letters_list)}")

end_of_game = False
live =6

while (not end_of_game):
    guess = input("guess a letter: ").lower()
    #for loop to check the guessed letter whether it is correct or not 
    for i in range(0,number_of_letters):
        if chosen_word[i] == guess:
            letters_list[i] = guess 
    
    #if guessed letter is incorrect u lose 1 live in game
    if guess not in chosen_word:
        live -=1
        if live == 0:
            end_of_game = True
            print("You Lose")
    
    print(f"{' '.join(letters_list)}")
    #If you guess all the letters without losing all your lives, you win
    if "_" not in letters_list:
        end_of_game = True
        print("you win")
    print(stages_hangman.stages[live])

print(f"Ooops ,The word to guess is {chosen_word}, good luck next time")