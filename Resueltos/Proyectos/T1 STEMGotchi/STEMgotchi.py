# ALVARO VILLANOVA AHLROTH      ESCUELA STEM GRANADA    2023
# STEMgotchi 0.3              

import random

######################  FUNCTIONS/ETC #############################
#----------------------    GRAPHICS   -----------------------------

# Refreshes the HUD to display the chosen menu:
def refreshCurrentScreenGFX(menuScreen):
    currentScreen=menuScreen
    return currentScreen
# Menu screens used to feed "currentScreenGFX" with different actions (start/main/stats/shop/inventory/etc screen)
def refreshSquareScreenGFX():
    squareScreenGFX[0]=f""" 
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n     
~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-( ),
; '/__\,.--';|   |[] .-.| O( _ )
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' ____   ''-,.   |
  ..    ..-'' |  |       ''. '
{promptSentence[0]}"""
    return squareScreenGFX[0]
def refreshIntroScreenGFX():
    introScreenGFX[0]=f""" 
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n     
              Welcome to...                               
 _____ _             _____     _       _   _ 
|   __| |_ ___ _____|   __|___| |_ ___| |_|_|
|__   |  _| -_|     |  |  | . |  _|  _|   | |
|_____|_| |___|_|_|_|_____|___|_| |___|_|_|_|

{promptSentence[0]}"""
    return introScreenGFX[0]
def refreshShopScreenGFX():
    shopScreenGFX[0]=f"""
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
 ___________________
/      ITEM SHOP    \\
               _ 
  Howdy      _| |_
   stranger! (o-o)
_____________/C\/|___
              
  Item 1: {itemShopInv[0]} {itemShopInvPrice[0]}     
  Item 2: {itemShopInv[1]} {itemShopInvPrice[1]}
  Item 3: {itemShopInv[2]} {itemShopInvPrice[2]}
   
\___________________/
Welcome to the shop!
{refreshLastAction()}
{promptSentence[0]} """
    return shopScreenGFX[0]
def refreshInfoScreenGFX():
    infoScreenGFX[0]=f"""
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
 ___________________
/________INFO_______\\ 
        {gotchiName}   
    Weight: {weight[0]}KG
       Age: {timeIteration[0]}
      Gold: {gold[0]}
    
 -{itemInv[0]} -{itemInv[1]}
 -{itemInv[2]} -{itemInv[3]}
 -{itemInv[4]} -{itemInv[5]}
 -{itemInv[6]} -{itemInv[7]}
 ____________________
\___________________/
{refreshLastAction()}""" 
    return infoScreenGFX[0]
def refreshGameOverScreenGFX():
    gameOverScreenGFX[0]=f""" 
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n     

 ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .                ▌ ▐·▄▄▄ .▄▄▄  
▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·         ▪     ▪█·█▌▀▄.▀·▀▄ █·
▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄          ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ 
▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌         ▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌
·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀           ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀ 
{gotchiName} died... Sorry! :(
Thank you for playing, bye! :)
"""
    return gameOverScreenGFX[0]
def refreshMainScreenGFX():
    mainScreenGFX[0]=f"""
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
 ___________________
/    STEMgotchi α   \\
     ¯¯¯¯¯¯¯¯¯¯¯¯ 
   {refreshSickGFX()}         {refreshPooGFX()}
     {refreshGotchiGFX()}     
           
 Hungry:{"🍗"*hungry[0]}          
  Happy:{"💖"*happiness[0]}
  Poo:{"💩"*droppings[0]}
   {sicknessStatus[0]}
\___________________/
{refreshLastAction()}
{promptSentence[0]}"""
    return mainScreenGFX[0]
# Refreshes different elements from screens (Poo/Poison/GotchiSprites/Last action sentence...)
def refreshGotchiGFX():
    # Refreshes gotchi's sprite, based on gotchi's state: BAD/OK/GREAT (Avg of hungry and happy)
    avgMood=happiness[0]+hungry[0]
    #Normalize mood just in case it goes below/over 0-10.
    if avgMood>8:
        avgMood=8
    elif avgMood<0:
        avgMood=0

    if avgMood<=2:
        gotchiGFX=gotchiSprites[0]
    elif avgMood>=6:
        gotchiGFX=gotchiSprites[2]
    else:
        gotchiGFX=gotchiSprites[1]
    return gotchiGFX
def refreshPooGFX():
    if droppings[0]==0:
        pooState=pooSprites[0]
    else:
        pooState=pooSprites[1]
    return pooState
def refreshSickGFX():
    if sickness[0]==False:
        sicknessStatus[0]="It's healthy! 😁"
        sicknessState=sicknessSprites[0]
    else:
        sicknessStatus[0]="It's sick. 🤢"
        sicknessState=sicknessSprites[1]
    return sicknessState
def refreshLastAction():
    if lastAction[0]==actions[0]:
        sentence=f"You fed {gotchiName} a {lastFoodUsed[0]}! "
    elif lastAction[0]==actions[1]:
        sentence=f"You played with {gotchiName}! "
    elif lastAction[0]==actions[2]:
        sentence=f"You cleaned up all the droppings! Yuck! "
    elif lastAction[0]==actions[4]:
        sentence=f"You cured {gotchiName}; It's feeling great now!"
    elif lastAction[0]==auxActions[0]:
        sentence=f"wrong choice! "
    elif lastAction[0]==auxActions[1]:
        sentence=f"You can't do that! Theres poo everywhere! "
    elif lastAction[0]==auxActions[2]:
        sentence=f"{gotchiName} it's already healthy, you can't do that. "
    elif lastAction[0]==auxActions[3]:
        sentence=f"{gotchiName} it's sick! You can't do that. "
    elif lastAction[0]==auxActions[4]:
        sentence=f"You can't afford it; Come again soon! "
    elif lastAction[0]==auxActions[5]:
        sentence=f"You already have this item in your inventory. Bye!"
    elif lastAction[0]==auxActions[6]:
        sentence=f"You don't have enough room in your inventory. See you! "
    elif lastAction[0]==auxActions[7]:
        sentence=f"Thanks for coming, bye!"
    elif lastAction[0]==auxActions[8]:
        sentence=f"Stop wasting my time! Come back when you wanna do some business. "
    elif lastAction[0]==auxActions[9]:
        sentence=""
    elif lastAction[0]==auxActions[10]:
        sentence=f"You won the game. Congrats! "
    elif lastAction[0]==auxActions[11]:
        sentence=f"You lost the game. Sorry, try again soon! "
    else:
        sentence=""
    return sentence

#---------------------   FUNCTIONAL  ------------------------------
# Refreshes time iteration (Also, droppings, shop and sickness mechanics happen here)
def refreshTimeIteration():
    # Shop rotation check
    if timeIteration[0]%9==0 or timeIteration[0]==1:
        counterShopRand=0
        for i in range(0,3):
            randomElement=random.randint(0,9)
            newItem=itemList[randomElement]
            newItemPrice=itemListPrice[randomElement]
            itemShopInv[counterShopRand]=newItem
            itemShopInvPrice[counterShopRand]=newItemPrice
            counterShopRand+=1
    # Droppings check
    if timeIteration[0]%3==0 and timeIteration[0]!=0:
        droppings[0]+=1
        if droppings[0]>maxDroppings[0]:
            droppings[0]=maxDroppings[0]
        happiness[0]-=1
        if happiness[0]<minHappiness[0]:
            happiness[0]=minHappiness[0]
    # Sickness check:
    if droppings[0]>=3:
        sickness[0]=True
# Action trees
def feedGotchi():
    if droppings[0]>=1:
        lastAction[0]=auxActions[1]
    else:
        promptSentence[0]=f"Feed {gotchiName} with meal or candy? "
        currentScreenGFX[0]=refreshCurrentScreenGFX(refreshMainScreenGFX())
        print(currentScreenGFX[0])
        mealOrCandy=input("")
        increaseHunger(mealOrCandy)       
def increaseHunger(mealOrCandy):
    if mealOrCandy=="candy":
        if sickness[0]==False:
            lastFoodUsed[0]="candy"
            hungry[0]+=1
            happiness[0]+=1
            weight[0]+=2
            timeIteration[0]+=1
            if hungry[0]>maxHunger[0]:
                hungry[0]=maxHunger[0]
            if happiness[0]>maxHappiness[0]:
                happiness[0]=maxHappiness[0]
            if weight[0]>maxWeight[0]:
                weight[0]=maxWeight[0]
            lastAction[0]=actions[0]
        else:
            lastAction[0]=auxActions[3]
    elif mealOrCandy=="meal":
        lastFoodUsed[0]="meal"
        hungry[0]+=1
        weight[0]+=1
        timeIteration[0]+=1
        if hungry[0]>maxHunger[0]:
            hungry[0]=maxHunger[0]
        if weight[0]>maxWeight[0]:
            weight[0]=maxWeight[0]
        lastAction[0]=actions[0]
    else:
        lastAction[0]=auxActions[0]
def playGotchi():
    if droppings[0]>=4 or sickness[0]==True:
        if droppings[0]>=4:
            lastAction[0]=auxActions[1]
        if sickness[0]==True:
            lastAction[0]=auxActions[3]
    else:
        print("\n"*50)
        playDecision=input("What do you want to play? (RPS/Hangman)").lower()
        if playDecision=="rps":
            print(rockPaperScissors())
        elif playDecision=="hangman":
            print(hangmanGame())
        else:
            return
def hangmanGame():
    attempts=8
    correctGuesses=0
    victoryPointsMultiplier=10
    victoryPointsBonus=20
    totalPoints=0
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
            totalPoints+=2
        elif chosenLetter not in gameWord:
            print("Wrong! Try again. ")
            totalPoints-=1
        else:
            print("Wrong! Try again. ")
        attempts-=1

        if len(gameWord)==correctGuesses:
            totalPoints=(totalPoints+victoryPointsBonus)*victoryPointsMultiplier
            gold[0]+=totalPoints
            print(f"Yes! {gameWord} was the correct word!")
            input(f"You score is {totalPoints}pts. You get {totalPoints}G!")
            increaseHappiness()
            foundTheWord=True
            lastAction[0]=auxActions[10]

    if attempts==0 and len(gameWord)!=correctGuesses:
        input("You lost the game... Try again soon! ")
        lastAction[0]=auxActions[11]
    timeIteration[0]+=1
def rockPaperScissors():
    rpsChoices=[1,2,3] # rock / paper / scissors
    totalRounds=3
    playerChoiceRPS=0
    playerWins=0
    npcChoice=0
    npcWins=0
    roundCounter=0

    while roundCounter!=totalRounds:
        npcChoice=random.choice(rpsChoices)
        playerChoiceRPS=int(input("Rock, paper or scissors? (1/2/3)"))
        print(f" NPC Chose: {npcChoice}")
        print(f" Player chose: {playerChoiceRPS}")

        if (npcChoice==1 and playerChoiceRPS==2) or (npcChoice==2 and playerChoiceRPS==3) or (npcChoice==3 and playerChoiceRPS==1):
            print(f"{gotchiName} won this round! ")
            playerWins+=1
            roundCounter+=1
        elif playerChoiceRPS==npcChoice:
            print("Draw! ")
        else:
            print(f"{gotchiName} lost this round! ")
            npcWins+=1
            roundCounter+=1

    if playerWins>npcWins:
        totalPoints=random.randint(100,200)
        gold[0]+=totalPoints
        input(f"You won this game! You get {totalPoints}G!")
        increaseHappiness()
        lastAction[0]=auxActions[10]
    else:
        input(f"You lost the game... Better luck next time.")
        lastAction[0]=auxActions[11]
    timeIteration[0]+=1
def increaseHappiness():
    happiness[0]+=1
    hungry[0]-=1
    weight[0]-=1
    if happiness[0]>maxHappiness[0]:
        happiness[0]=maxHappiness[0]
    if hungry[0]<minHunger[0]:
        hungry[0]=minHunger[0]
    if weight[0]<minWeight[0]:
        weight[0]=minWeight[0]
    timeIteration[0]+=1
    lastAction[0]=actions[1]
def cleanGotchi():
    droppings[0]=0
    lastAction[0]=actions[2]
    timeIteration[0]+=1
def cureGotchi():
    if sickness[0]==False:
        lastAction[0]=auxActions[2]
    elif droppings[0]!=0:
        lastAction[0]=auxActions[1]
    else:
        sickness[0]=False
        timeIteration[0]+=1
        lastAction[0]=actions[4]
def infoGotchi():
    auxVariable=" "
    auxVariable=input("You're in the INFO screen. Press ENTER to return.")
    if timeIteration[0]%3==0:
        droppings[0]-=1
def shopGotchi():
    itemToBuy=input("")
    buyItemFromShop(itemToBuy)
def buyItemFromShop(itemToBuy):
    if itemToBuy=="1" or itemToBuy=="2" or itemToBuy=="3":
        itemToBuy=int(itemToBuy)
    else:
        lastAction[0]=auxActions[8]
        return
    if itemToBuy==1 or itemToBuy==2 or itemToBuy==3:
        if gold[0]>=itemShopInvPrice[itemToBuy-1] and itemInv.count(itemShopInv[itemToBuy-1])==0 and itemInv.count("        ")>0:
            gold[0]-=itemShopInvPrice[itemToBuy-1]
            itemBought=1
            slotCounter=0
            for slot in itemInv:
                if slot=="        " and itemBought==1:
                    itemInv[slotCounter]=itemShopInv[itemToBuy-1]
                    itemBought=0
                    lastAction[0]=auxActions[7]
                    timeIteration[0]+=1
                slotCounter+=1
        elif gold[0]<itemShopInvPrice[itemToBuy-1]:
            lastAction[0]=auxActions[4]
        elif itemInv.count(itemShopInv[itemToBuy-1])>0:
            lastAction[0]=auxActions[5]
        elif itemInv.count("        ")==0:
            lastAction[0]=auxActions[6] 



        


    
##################   LISTS AND VARIABLES  ###########################
#----------------------    GRAPHICS   -------------------------------

# Graphics, Sprites and sentences used by "currentScreenGFX".
pooSprites=["","༼ ༽ɞ"]
pooState=""
gotchiSprites=["( `ε´ )","(´･ᴗ･ `)","(o˘◡˘o)"]
gotchiGFX=[""]
sicknessSprites=["","🕱"]
sicknessState=""
sicknessStatus=[""]
currentScreenGFX=[""]
mainScreenGFX=[""]
infoScreenGFX=[""]
introScreenGFX=[""]
shopScreenGFX=[""]
squareScreenGFX=[""]
gameOverScreenGFX=[""]
lastAction=[""]
lastFoodUsed=[""]
promptSentence=[""]


# -------------------------- FUNCTIONAL ---------------------------------

# Action lists to use in action tree.
actions=["feed","play","clean","cure","info","shop","square"]
auxActions=["wrongAction","gottaClean","alreadyHealthy","currentlySick","notEnoughGold","itemInPosession","noInvSpace","boughtSomething","wrongShopChoice","clearLastAction","wonGame","lostGame"]
itemInv=["        ","        ","        ","        ","        ","        ","        ","        ",]
itemList=["⚾Ball  ","🧢Hat   ","⛸️ Skates","🛹SBoard","🖍️ Pencl","🏸Racket","👢Boots ","🎷Sax   ","📿NkLace","🪁Kite  "]
itemListPrice=[50,200,500,900,100,350,400,1000,250,150]
itemShopInv=["        ","        ","        "]
itemShopInvPrice=[0,0,0]


# Innit values

sickness=[False]
gotchiName=""
hungry=[0]
happiness=[0]
droppings=[0]
weight=[1]
timeIteration=[99]
gold=[2500]
# min/max values
minHunger=[0]
maxHunger=[4]
minHappiness=[0]
maxHappiness=[4]
minDroppings=[0]
maxDroppings=[6]
minWeight=[1]
maxWeight=[99]


#######################################################################
##########################   MAIN CODE   ##############################
#######################################################################

gameLoop=True


while len(gotchiName)>5 or len(gotchiName)==0:
    promptSentence[0]="↓  Choose your gotchi's name (max. 5 characters):  ↓"
    currentScreenGFX[0]=refreshCurrentScreenGFX(refreshIntroScreenGFX())
    print(currentScreenGFX[0])
    gotchiName=input()


while gameLoop:
    refreshTimeIteration()
    promptSentence[0]="What to do now? (feed/clean/cure/info/square): "
    currentScreenGFX[0]=refreshCurrentScreenGFX(refreshMainScreenGFX())
    print(currentScreenGFX[0])
    decision=""
    while decision=="":
        decision=input()
        decision.lower() 
        if decision==actions[0]: # PLAYER CHOOSES FEED
            feedGotchi()
        elif decision==actions[2]: # PLAYER CHOOSES CLEAN
            cleanGotchi()
        elif decision==actions[3]: # PLAYER CHOOSES CURE 
            cureGotchi()
        elif decision==actions[4]: # PLAYER CHOOSES INFO 
            currentScreenGFX[0]=refreshCurrentScreenGFX(refreshInfoScreenGFX())
            print(currentScreenGFX[0])
            infoGotchi()
        elif decision==actions[6]: # PLAYER CHOOSES SQUARE
            promptSentence[0]="Welcome to the Town Square! (play/shop) "
            lastAction[0]=auxActions[9]
            currentScreenGFX[0]=refreshCurrentScreenGFX(refreshSquareScreenGFX())
            print(currentScreenGFX[0])
            decision=input("")
            if decision==actions[5]: # PLAYER CHOOSES SHOP
                promptSentence[0]="What are you buying sirr? (1/2/3) "
                lastAction[0]=auxActions[9]
                currentScreenGFX[0]=refreshCurrentScreenGFX(refreshShopScreenGFX())
                print(currentScreenGFX[0])
                shopGotchi()
            elif decision==actions[1]: # PLAYER CHOOSES PLAY
                playGotchi()
            else:
                lastAction[0]=auxActions[0]
        else: # PLAYER CHOOSES ANYTHING ELSE (ERROR)
            lastAction[0]=auxActions[0]
        gameLoop=timeIteration[0]!=100 # Shuts down the game loop if we get to 100 iterations


currentScreenGFX[0]=refreshCurrentScreenGFX(refreshGameOverScreenGFX())
print(currentScreenGFX[0])


