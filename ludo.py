import random
class Game:
    def __init__(self):
        pass




    def rollingDice(self):
        #print message of options you have when you roll 6
        def printOptionsMessage():
            print() #TODO
        #rolling a dice
        #message TODO?
        numberRolled = random.randint(1, 6)

        if numberRolled == 6:   #if 6 is rolled
            printOptionsMessage() 
            choice = input()    #choice of a player
            while choice != 'new' and choice != 'move': #testing validity
                print('Invalid option type it again')
                printOptionsMessage()
                choice = input()
            
            if choice == 'new':
                newPawn()   #TODO
            if choice == 'move':
                movingPawn()    #TODO

    def printPlayer()


