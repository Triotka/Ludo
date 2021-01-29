import random

class Pawn(): #TODO
    def __init__(self ,board):
        self.positionColumn
        self.positionRow
        self.color
    def move(self): #TODO
        pass
    def remove(self): #TODO
        pass
class Game:
    def __init__(self):
        self.sizeBoard = 17
        self.board = [[0] for i in range(self.sizeBoard)]
        self.turn = 1
        self.numberOfPlayers = 1
        pass
   #sets yard on the board
    def setYards(self):

         #set a yard of size 7x7 filled with color of a player on certain position 
        def setYard(startUpRow, startLeftColumn, filling):
            sizeofYard = 7

            assert sizeofYard + startLeftColumn < self.sizeBoard and sizeofYard + startUpRow < self.sizeBoard, 'Yard is out of board'
            for i in range(sizeofYard):
                
                self.board[startUpRow][startLeftColumn + i] = filling #up boundary
                self.board[startUpRow + sizeofYard - 1][startLeftColumn + i] = filling  #down boundary
                self.board[startUpRow + i][startLeftColumn] = filling    #left boundary
                self.board[startUpRow + i][startLeftColumn + sizeofYard - 1] = filling    #rightboundary
            
            # colors places for pawns
            self.board[startUpRow + 2][startLeftColumn + 2] = filling
            self.board[startUpRow + 2][startLeftColumn + 4] = filling
            self.board[startUpRow + 4][startLeftColumn + 2] = filling
            self.board[startUpRow + 4][startLeftColumn + 4] = filling

    #set yard of players

    def setNumberOfPlayers(self):
        pass

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