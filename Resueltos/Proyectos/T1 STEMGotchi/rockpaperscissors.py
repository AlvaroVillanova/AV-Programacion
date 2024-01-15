import random


def rockPaperScissors():
    rpsChoices=[1,2,3] # rock / paper / scissors
    totalRounds=3
    playerChoice=0
    playerWins=0
    npcChoice=0
    npcWins=0
    roundCounter=0

    while roundCounter!=totalRounds:
        npcChoice=random.choice(rpsChoices)
        playerChoice=int(input("Rock, paper or scissors? (1/2/3)"))
        print(f" NPC Chose: {npcChoice}")
        print(f" Player chose: {playerChoice}")

        if (npcChoice==1 and playerChoice==2) or (npcChoice==2 and playerChoice==3) or (npcChoice==3 and playerChoice==1):
            print(f"{gotchiName} won this round! ")
            playerWins+=1
            roundCounter+=1
        elif playerChoice==npcChoice:
            print("Draw! ")

        else:
            print(f"{gotchiName} lost this round! ")
            npcWins+=1
            roundCounter+=1

    if playerWins>npcWins:
        gameWinner=f"{gotchiName} won this game! "
    else:
        gameWinner=f"{gotchiName} lost the game! "
    return gameWinner
def hangmanGame():
    attempts=8
    correctGuesses=0
    foundTheWord=False
    foundLetters=[]
    listaPalabras=["computer","elephant","guitar","happiness","star","garden","mountain","universe","library","butterfly","telephone","chocolate","adventure","calendar","dog","hat","cloud","journey","painting","winter","ocean","scarf","choice","pencil","piano","walk","party","serenity","breakfast","kite"]
    gameWord=random.choice(listaPalabras)
    findingWord="_"*len(gameWord)

    while foundTheWord==False and attempts>0:
        chosenLetter=""
        findingWord=gameWord


        for letter in findingWord:
            if letter in foundLetters:
                print(letter, end="")
            else:
                letter="_"
                print(letter, end="")
        print("")



        while len(chosenLetter)!=1 and chosenLetter.isalpha()==False:
            chosenLetter=""
            chosenLetter=input(f"You got {attempts} attempts left. Choose a letter: ")

        if chosenLetter in foundLetters:
            print("You already found that letter! ")
        elif chosenLetter in gameWord and len(chosenLetter)==1:
            foundLetters.append(chosenLetter)
            print("Thats correct! ")
            correctGuesses+=1
        elif chosenLetter not in gameWord:
            print("Wrong! Try again. ")
        else:
            print("Wrong! Try again. ")
        attempts-=1

        if len(gameWord)==correctGuesses:
            print(f"Yes! {gameWord} was the correct word!")
            result="Congrats! You won the game. "
            foundTheWord=True

    if attempts==0 and len(gameWord)!=correctGuesses:
        result="You lost the game... Try again soon! "
    return result

gotchiName="Pepe"

###########################   RPS    ############################

#print(rockPaperScissors())


########################  Hangman   #############################################

print(hangmanGame())




