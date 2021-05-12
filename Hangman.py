#Shriharsh Vinod Patil

import random

def hangman():                                          #main method of the Game i.e Hangman
    word = random.choice(["ironman","superman","spiderman","thor","hulk","doctorstrange","falcon","antman","batman","blackwidow","captainamerica","groot","rocket","wanda","vision","loki","blackpanther"])
    valid_letter = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guess_made = ''

    while(len(word)>0):                                 #this loop checks the woed length and created main string
        main = ""
        missed = 0

        for letter in word:                                 #this loop checks if the letters are in the word or not
            if letter in guess_made:
                main += letter
            else:
                main += "_" + " "

        if main == word:
            print(main)
            print("Congaratution {} , You WON !!!!!!!!!" .format(name))
            break

        print("Guess the Word " , main )
        guess = input()

        if guess in valid_letter:                           #this condition checks if the letter is valid or not
            guess_made += guess
        else:
            print("Enter a valid Character ")
            guess = input()


        if guess not in word:                               #this condition is for checking word and turns remaining
            turns -= 1
            print ("Wrong Guess !!!!!")
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose!!!!!!")
                print("You let a kind man die!!!!!!")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name =  input("Enter Your Name : ")
print("Welcome {}, to  the HANGMAN game!!!! ".format(name))
print("\n---------------------------------------\n")
hint = input("press y to show hint and n to continue with Hint\n")
if hint == 'y':
    print("\nAll the words are of Superheores name !!!!!!\n")
hangman()
