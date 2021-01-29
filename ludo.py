import random
class Game:
    def __init__(self):
        self.turn = 1
        self.numberOfPlayers = 1
        pass
    def setNumberOfPlayers(self):

    def newPawn(self):  #TODO
        print('new pawn')

    def movingPawn(self): #TODO
        print('moving pawn')



    #switch to the next Player
    def switchPlayer(self):
        self.turn = (self.turn + 1) % (self.numberOfPlayers) + 1

    def rollingDice(self):
        #print message of options you have when you roll 6
        def printOptionsMessage():
            print('TODO message for choice') #TODO
       
        #rolling a dice
        print('Rolling a dice ...')
        numberRolled = random.randint(1, 6)
        print('Number rolled is:', numberRolled)

        if numberRolled == 6:   #if 6 is rolled
            printOptionsMessage() 
            choice = input()    #choice of a player
            while choice != 'new' and choice != 'move': #testing validity
                print('Invalid option type it again')
                printOptionsMessage()
                choice = input()
            
            if choice == 'new':
                self.newPawn()   #TODO
            if choice == 'move':
                self.movingPawn()    #TODO

    def printPlayer(self):   #TODO
        pass

    


game = Game()
while(True):
    game.rollingDice()