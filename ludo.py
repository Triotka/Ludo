import random






    
class Pawn(): #TODO
    def __init__(self, positionRow, positionColumn, color, name):
        
        self.positionColumn = positionColumn #column in which it is on the board
        self.positionRow = positionRow  #row in which it is on the board   
        self.color = color
        self.name = name    #name visible on the board
        self.directionColumn = 0    #direction for next move for the column
        self.directionRow = 0   #direction for next move for the row

     #moving the pawn by number of moves on the board   
    def move(self, numberOfMoves, board): #TODO
        
        #moves pawn one grid in proper direction and returns a board with this change
        def go():
             board.board[self.positionRow][self.positionColumn] = 0
             self.positionColumn += self.directionColumn
             self.positionRow += self.directionRow
             board.board[self.positionRow][self.positionColumn] = self.name
             return board
             
        #turning a pawn down
        def turnDown():
            self.directionRow = 1
            self.directionColumn = 0

        #turning a pawn up
        def turnUp():
            self.directionRow = -1
            self.directionColumn = 0

        #turning a pawn right
        def turnRight():
            self.directionRow = 0
            self.directionColumn = 1
        
        #turning a pawn left
        def turnLeft():
            self.directionRow = 0
            self.directionColumn = -1
        
        #turning paw when it is on the certain grid
        def turning():

            
            if self.positionRow == 0:   # border on the top
                if self.positionColumn == board.sizeOfYard: #left one
                    turnRight()           
                elif self.positionColumn == board.sizeOfYard + 2: #right one
                    turnDown()
            elif self.positionRow == board.sizeBoard - 1:   # border on the bottom
                if self.positionColumn == board.sizeOfYard: #left one
                    turnUp()           
                elif self.positionColumn == board.sizeOfYard + 2:   #right one
                    turnLeft()


            if self.positionColumn == 0:   #border on the left
                if self.positionRow == board.sizeOfYard:    #top one
                    turnRight()
                elif self.positionRow == board.sizeOfYard + 2:  #bottom one
                    turnUp()
            
            elif self.positionColumn == board.sizeBoard - 1:  #border on the right
                if self.positionRow == board.sizeOfYard:    #top one
                    turnDown()
                elif self.positionRow == board.sizeOfYard + 2:  #bottom one
                    turnLeft()

            #middle
            elif self.positionColumn == board.sizeOfYard:
                if self.positionRow == board.sizeOfYard:    #top one
                    turnUp()
                elif self.positionRow == board.sizeOfYard + 2:  #bottom one
                    turnLeft()
            elif self.positionColumn == board.sizeOfYard + 2:
                if self.positionRow == board.sizeOfYard:    #top one
                    turnRight()
                elif self.positionRow == board.sizeOfYard + 2:  #bottom one
                    turnDown()
            

        for i in range(numberOfMoves):
           turning()
           go()


           


    def remove(self): #TODO
         pass  


class Board:
    def __init__(self):
        self.sizeBoard = 17
        self.board = [['-'] * self.sizeBoard for _ in range(self.sizeBoard)]
        self.sizeOfYard = 7
        self.sizeOfHouse = 5
    

   #sets yards on the board
    def setYards(self):
    
         #sets a yard of size 7x7 filled with color of a player on certain position 
        def setYard(startUpRow, startLeftColumn, filling):
            
            assert self.sizeOfYard + startLeftColumn <= self.sizeBoard and self.sizeOfYard + startUpRow <= self.sizeBoard, 'Yard is out of board'
            
            for i in range(self.sizeOfYard):   
                self.board[startUpRow][startLeftColumn + i] = filling #up boundary
                self.board[startUpRow + self.sizeOfYard-1][startLeftColumn + i] = filling  #down boundary
                self.board[startUpRow + i][startLeftColumn] = filling    #left boundary
                self.board[startUpRow + i][startLeftColumn + self.sizeOfYard - 1] = filling    #rightboundary
            
            # colors places for pawns
            self.board[startUpRow + 2][startLeftColumn + 2] = filling
            self.board[startUpRow + 2][startLeftColumn + 4] = filling
            self.board[startUpRow + 4][startLeftColumn + 2] = filling
            self.board[startUpRow + 4][startLeftColumn + 4] = filling

    #set yard of players
        setYard(0, 0, 1)
        setYard(0, self.sizeBoard - self.sizeOfYard, 2)
        setYard(self.sizeBoard - self.sizeOfYard, self.sizeBoard - self.sizeOfYard, 3)
        setYard(self.sizeBoard - self.sizeOfYard, 0, 4)


    #sets houses on the board
    def setHouses(self):
        
        #sets house filled with color of a player on certain position and direction
        def setHouse(startRow, startColumn, direction, filling):
            assert direction == 'LR' or direction =='UD', 'wrong direction'
            for i in range(self.sizeOfHouse):
                if direction =='LR':    #from left to right
                    self.board[startRow][startColumn + i] = filling
                if direction =='UD': #from up down
                    self.board[startRow + i][startColumn] = filling



        setHouse(self.sizeOfYard + 1, 1, 'LR', 1)
        setHouse(self.sizeOfYard + 1, self.sizeBoard - self.sizeOfHouse - 1, 'LR', 3)
        setHouse(1, self.sizeOfYard + 1, 'UD', 2)
        setHouse(self.sizeBoard - self.sizeOfHouse - 1, self.sizeOfYard + 1, 'UD', 4)    

    #sets starts on the board
    def setStarts(self):    #TODO
        pass
    #creates a board with yards and houses
    def createBoard(self):
        self.setHouses()
        self.setYards()

    def printingBoard(self):    #TODO
        for i in range(self.sizeBoard):
            s =''
            for j in range(self.sizeBoard):
                s += str(self.board[i][j]) + ' '
            print(s)
        print(' ')



class Game:
    def __init__(self):
        self.boardPawns = Board()
        self.turn = 1
        self.numberOfPlayers = 1


    def settingPawns(self):
        pawns_player_1 = []
        pawns_player_2 = []
        pawns_player_3 = []
        pawns_player_4 = []

        def givingPawsToPlayer(player, listOfPaws, yardRow, yardColumn):
            #setting four pawns
                listOfPaws.append(Pawn(yardRow, yardColumn,  player, str(player) + '1'))
                listOfPaws.append(Pawn(yardRow, yardColumn + 2, player, str(player) +'2'))
                listOfPaws.append(Pawn(yardRow + 2, yardColumn, player, str(player) +'3'))
                listOfPaws.append(Pawn(yardRow + 2, yardColumn + 2, player, str(player) +'4'))

                #putting it on the board with pawns
                for paw in listOfPaws:
                    self.boardPawns[paw.positionRow][paw.positionColumn] = paw.name
                    
    #TODO  call Pawns

    def setNumberOfPlayers(self):
        self.setNumberOfPlayers = int(input)

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
    def isOver(self): #TODO
        pass

    def play(self):
        board = Board()
        while(self.isOver() == False):
            board.show()

            self.rollingDice()


# while(True):
#     game.rollingDice()

test = Board()
test.createBoard()

p = Pawn(0, 7, 'green', 'G' + '1')
for i in range(20):
    p.move(5, test)
    test.printingBoard()



