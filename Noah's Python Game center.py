while True:
    print("Welcome to Noah Gaviña's Python Game center.")
    print("--------------------------------------------")
    print("|                                          |")
    print("|     Welcome                              |")
    print("|Please select the game you want to play.  |")
    print("| 1. Noah's Hangman                        |")
    print("| 2. Noah's Guessing Game                  |")
    print("| 3. Noah's ABC Game                       |")
    print("| 4. Jorge's Tic-Tac-Toe Game              |")
    print("| 5. Jy'Chaun's Blackjack Game             |")
    print("|                                          |")
    print("| Just hit enter without any value to quit.|")
    print("If you start Jy'Chaun's game it will end if you put q for quit.")
    print("--------------------------------------------")
    gameChoice = int(input())
    if gameChoice == 1:
        import random
        name = input("Hello, what is your name?:")
        if name == "whiteface":
            exit()
        print("Ok " + name + " let's play hangman.")

        HANGMANPICS = ['''

              +---+
              |   |
                  |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              0   |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              0   |
              |   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              0   |
             /|   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              0   |
             /|\  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              0   |
             /|\  |
             /    |
                  |
            =========''', '''
              +---+
              |   |
              0   |
             /|\  |
             / \  |
                  |
            =========''']
        words = 'lumbago doom wolfenstein arthur morgan uncle john marston depression anxiety autism noah gavina sebastian pamela manuel chainsaw fist pistol shotgun super chaingun rocket launcher whiteface persona shadow self facade mask cat bear android fool magician priestess empress emperor hierophant lovers chariot justice hermit fortune strength hangman death temperance devil tower star moon sun judgement world psyche'.split()

        def getRandomWord(wordList):
            #This gets a random word from the list.
            wordIndex = random.randint(0, len(wordList) - 1)
            return wordList[wordIndex]

        def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
            print(HANGMANPICS[len(missedLetters)])
            print()

            print('Missed letters:', end=' ')
            for letter in missedLetters:
                    print(letter, end=' ')
            print()

            blanks = '_' * len(secretWord)

            for i in range(len(secretWord)): #This will replace the blanks with the letters
                if secretWord[i] in correctLetters:
                    blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

            for letter in blanks: #Shows the secret word with spaces in between each letter
                print(letter, end=' ')
            print()

        def getGuess(alreadyGuessed):
            # This returns the letter entered and makes sure it is only a single letter.
            while True:
                print('Guess a letter.')
                guess = input()
                guess = guess.lower()
                if len(guess) != 1:
                    print('Please enter a single letter.')
                elif guess in alreadyGuessed:
                    print('You have already guessed that letter. Choose another.')
                elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                    print('Please enter a LETTER, not a number or other character.')
                else:
                    return guess
        def playAgain():
            #True if player wants to play again otherwise False.
            print('Do you want to play again? (yes or no)')
            return input().lower().startswith('y')
        def wordBank():
            #True if the player wants to see the word bank
            print('Would you like a word bank before you start? (yes or no)')
            return input().lower().startswith('y')
        if wordBank():
            print('The words are as follows:')
            print('lumbago doom wolfenstein arthur morgan uncle john marston depression anxiety autism noah gavina sebastian pamela manuel chainsaw fist pistol shotgun super chaingun rocket launcher whiteface persona shadow self facade mask cat bear android fool magician priestess empress emperor hierophant lovers chariot justice hermit fortune strength hangman death temperance devil tower star moon sun judgement world psyche')

        print('H A N G M A N')
        missedLetters = ''
        correctLetters = ''
        secretWord = getRandomWord(words)
        gameIsDone = False

        while True:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

            #Let the player type in a letter.
            guess = getGuess(missedLetters + correctLetters)

            if guess in secretWord:
                correctLetters = correctLetters + guess

                #Check if the player has won
                foundAllLetters = True
                for i in range(len(secretWord)):
                    if secretWord[i] not in correctLetters:
                        foundAllLetters = False
                        break
                if foundAllLetters:
                    print('Yes! the secret word was "' +secretWord + '"! You have won!')
                    gameIsDone = True
            else:
                missedLetters = missedLetters + guess

                #Check if the player guessed too much and lost
                if len(missedLetters) == len(HANGMANPICS) - 1:
                    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                    print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                    gameIsDone = True

            #Ask the player if they want to play again (only if the game is done).
            if gameIsDone:
                if wordBank():
                    print('the words are as follows:')
                    print('lumbago doom wolfenstein arthur morgan uncle john marston depression anxiety autism noah gavina sebastian pamela manuel chainsaw fist pistol shotgun super chaingun rocket launcher whiteface persona shadow self facade mask cat bear android fool magician priestess empress emperor hierophant lovers chariot justice hermit fortune strength hangman death temperance devil tower star moon sun judgement world psyche')
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = getRandomWord(words)
                else:
                    break
        input("Goodbye " + name + "!")

    elif gameChoice == 2:
            import random

            guessesTaken=0
            name=input("Hello user, what is your name?: ")
            if name == "whiteface":
                exit()
            number = random.randint(1,100)
            print("Ok " +name+ " let's play a guessing game.")
            print("The number is between 1 and 100 and you have about 50 guesses.")
            print("ONLY GUESS IN NUMBERS, OTHERWISE I WILL DIE.")
            while guessesTaken < 50:
                print("Take a guess now.:")
                guess = input()
                guess = int(guess)

                guessesTaken=guessesTaken+1

                if guess<number:
                    print("Higher.")

                if guess>number:
                    print("Lower.")

                if guess==number:
                    break
            if guess == number:
                guessesTaken=str(guessesTaken)
                print("Good job " +name+ ". You guessed the number in " +guessesTaken+ " guess(es).")
                print("I am going to send you back to the game center and forget you now, goodbye " +name+ ".")

            if guess != number:
                number = str(number)
                print("Wrong. The number I was thinking of was " +number)
                print("I am going to send you back to the game center and forget you now, goodbye " +name+ ".")

    elif gameChoice == 3:
            name = input("Hello user, what is your name?:")
            if name == "whiteface":
                exit()
            print("Hmm, " +name+ ", interesting...")
            print("I am going to order 3 numbers in order from greatest to least for you.")
            print("ONLY INSERT NUMBERS OR I WILL CRASH AND MY BLOOD WILL BE ON YOUR HANDS.")
            print("Also do not put in any duplicates, it will not kill me but I do not know how to process it.")
            a=int(input("What will number a be?:"))
            b=int(input("What will number b be?:"))
            c=int(input("What will number c be?:"))
            if (a>b) and (a>c) and (b>c):
                print("Then the order is:")
                print(a,b,c)
            if (a>b) and (a>c) and (b<c):
                print("Then the order is:")
                print(a,c,b)
            if (a<b) and (b>c) and (c<a):
                print("Then the order is:")
                print(b,a,c)
            if (a<b) and (b>c) and (c>a):
                print("Then the order is:")
                print(b,c,a)
            if (a<b) and (b<c):
                print("Then the order is:")
                print(c,b,a)
            if (a>b) and (a<c):
                print("Then the order is:")
                print(c,a,b)
            print("Thank you for playing with me, I am going to send you back to the game center and forget you now, goodbye "+name+".")

    elif gameChoice == 4:
        import random
        board = [0,1,2,3,4,5,6,7,8]
        def showboard():
            print (str(board[0])," | "+str(board[1])," | "+str(board[2]))
            print ('----------')
            print (str(board[3])," | "+str(board[4])," | "+str(board[5]))
            print ('----------')
            print (str(board[6])," | "+str(board[7])," | "+str(board[8]))
        def checking(char, spot1, spot2, spot3):
            if board[spot1] == char and board[spot2] == char and board[spot3] == char:
                return True
        def check(char):
            if checking(char, 0, 1, 2):
                return True
            if checking(char, 3, 4, 5):
                return True
            if checking(char, 6, 7, 8):
                return True
            if checking(char, 2, 4, 6):
                return True
            if checking(char, 0, 3, 6):
                return True
            if checking(char, 1, 4, 7):
                return True
            if checking(char, 2, 5, 8):
                return True
            if checking(char, 0, 4, 8):
                return True
        while True:
            number = input("Select a number: ")
            number = int(number)
            if board[number] != 'x' and board[number] != 'o':
                board[number] = 'x'
                if check('x') == True:
                    print ("X Wins!")
                    break
                while True:
                    number2 = random.randint(0,8)
                    if board[number2] != 'x' and board[number2] != 'o':
                        board[number2] = 'o'
                        showboard()
                        if check('o') == True:
                            print ("O Wins!")
                            break
                        break
            else:
                print ("Spot Taken... Try again.")
                break

    elif gameChoice == 5:
        import os
        import random

        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

        def deal(deck):
            hand = []
            for i in range(2):
                    random.shuffle(deck)
                    card = deck.pop()
                    if card == 11:card = "J"
                    if card == 12:card = "Q"
                    if card == 13:card = "K"
                    if card == 14:card = "A"
                    hand.append(card)
            return hand

        def play_again():
            again = input("Do you want to play again? (Y/N) : ").lower()
            if again == "y":
                    dealer_hand = []
                    player_hand = []
                    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
                    game()
            else:
                    print("Bye!")
                    

        def total(hand):
            total = 0
            for card in hand:
                    if card == "J" or card == "Q" or card == "K":
                        total+= 10
                    elif card == "A":
                        if total >= 11: total+= 1
                        else: total+= 11
                    else: total += card
            return total

        def hit(hand):
                card = deck.pop()
                if card == 11:card = "J"
                if card == 12:card = "Q"
                if card == 13:card = "K"
                if card == 14:card = "A"
                hand.append(card)
                return hand

        def clear():
                if os.name == 'nt':
                        os.system('CLS')
                if os.name == 'posix':
                        os.system('clear')

        def print_results(dealer_hand, player_hand):
                clear()
                print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
                print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

        def blackjack(dealer_hand, player_hand):
                if total(player_hand) == 21:
                        print_results(dealer_hand, player_hand)
                        print ("Congratulations! You got a Blackjack!\n")
                        play_again()
                elif total(dealer_hand) == 21:
                        print_results(dealer_hand, player_hand)		
                        print ("Sorry, you lose. The dealer got a blackjack.\n")
                        play_again()

        def score(dealer_hand, player_hand):
                if total(player_hand) == 21:
                        print_results(dealer_hand, player_hand)
                        print ("Congratulations! You got a Blackjack!\n")
                elif total(dealer_hand) == 21:
                        print_results(dealer_hand, player_hand)		
                        print ("Sorry, you lose. The dealer got a blackjack.\n")
                elif total(player_hand) > 21:
                        print_results(dealer_hand, player_hand)
                        print ("Sorry. You busted. You lose.\n")
                elif total(dealer_hand) > 21:
                        print_results(dealer_hand, player_hand)			   
                        print ("Dealer busts. You win!\n")
                elif total(player_hand) < total(dealer_hand):
                        print_results(dealer_hand, player_hand)
                #print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
                elif total(player_hand) > total(dealer_hand):
                        print_results(dealer_hand, player_hand)			   
                        print ("Congratulations. Your score is higher than the dealer. You win\n")		

        def game():
                choice = 0
                clear()
                print ("WELCOME TO BLACKJACK!\n")
                dealer_hand = deal(deck)
                player_hand = deal(deck)
                while choice != "q":
                        print ("The dealer is showing a " + str(dealer_hand[0]))
                        print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
                        blackjack(dealer_hand, player_hand)
                        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
                        clear()
                        if choice == "h":
                                hit(player_hand)
                                while total(dealer_hand) < 17:
                                        hit(dealer_hand)
                                score(dealer_hand, player_hand)
                                play_again()
                        elif choice == "s":
                                while total(dealer_hand) < 17:
                                        hit(dealer_hand)
                                score(dealer_hand, player_hand)
                                play_again()
                        elif choice == "q":
                                print ("Bye!")
                                
                
        if __name__ == "__main__":
            game()





