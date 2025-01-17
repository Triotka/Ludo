import random
   
class Pawn(): #TODO
    def __init__(self, positionRow, positionColumn, player, name):
        
        self.positionColumn = positionColumn #column in which it is on the board
        self.positionRow = positionRow  #row in which it is on the board   
        self.player = player
        self.name = name    #name visible on the board
        self.directionColumn = 0    #direction for next move for the column
        self.directionRow = 0   #direction for next move for the row
        self.goingToHouse = False
        self.gridInHouse = 0 #on which grid in the house it is

     #moving the pawn by number of moves on the board   
    def move(self, numberOfMoves, locationOfPawns):
        #position of a pawn before moving
        previousPositionRow = self.positionRow
        previousPositionColumn =  self.positionColumn
        movesToHouse = 0
        
        #moves pawn one grid in proper direction and returns a board with this change
        def go():
             self.positionColumn += self.directionColumn
             self.positionRow += self.directionRow
             
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
                if self.positionColumn == locationOfPawns.sizeOfYard: #left one
                    turnRight()           
                elif self.positionColumn == locationOfPawns.sizeOfYard + 2: #right one
                    turnDown()
            elif self.positionRow == locationOfPawns.sizeBoard - 1:   # border on the bottom
                if self.positionColumn == locationOfPawns.sizeOfYard: #left one
                    turnUp()           
                elif self.positionColumn == locationOfPawns.sizeOfYard + 2:   #right one
                    turnLeft()

            if self.positionColumn == 0:   #border on the left
                if self.positionRow == locationOfPawns.sizeOfYard:    #top one
                    turnRight()
                elif self.positionRow == locationOfPawns.sizeOfYard + 2:  #bottom one
                    turnUp()
            
            elif self.positionColumn == locationOfPawns.sizeBoard - 1:  #border on the right
                if self.positionRow == locationOfPawns.sizeOfYard:    #top one
                    turnDown()
                elif self.positionRow == locationOfPawns.sizeOfYard + 2:  #bottom one
                    turnLeft()

            #middle
            elif self.positionColumn == locationOfPawns.sizeOfYard:
                if self.positionRow == locationOfPawns.sizeOfYard:    #top one
                    turnUp()
                elif self.positionRow == locationOfPawns.sizeOfYard + 2:  #bottom one
                    turnLeft()
            elif self.positionColumn == locationOfPawns.sizeOfYard + 2:
                if self.positionRow == locationOfPawns.sizeOfYard:    #top one
                    turnRight()
                elif self.positionRow == locationOfPawns.sizeOfYard + 2:  #bottom one
                    turnDown()

            #position of entering to house
            if self.player == 1:
                if self.positionRow == locationOfPawns.sizeOfYard + 1 and self.positionColumn == 0:
                    turnRight()
                    self.goingToHouse = True

            if self.player == 2:
                if self.positionRow == 0 and self.positionColumn == locationOfPawns.sizeOfYard + 1:
                    turnDown()
                    self.goingToHouse = True

            if self.player == 3:
                if self.positionRow == locationOfPawns.sizeOfYard + 1 and self.positionColumn == locationOfPawns.sizeBoard - 1:
                    turnLeft()
                    self.goingToHouse = True
            if self.player == 4:
                if self.positionRow == locationOfPawns.sizeBoard - 1 and self.positionColumn == locationOfPawns.sizeOfYard + 1:
                    turnUp()
                    self.goingToHouse = True
                
        

        
        locationOfPawns.board[previousPositionRow][previousPositionColumn] = 0
        for i in range(numberOfMoves):
           
           turning()
           
           
           #checking if there is a pawn from someone else if so kill it
           if i == numberOfMoves - 1:
               grid = locationOfPawns.board[self.positionRow + self.directionRow][self.positionColumn + self.directionColumn]
               if isinstance(grid, Pawn):
                    if grid.player == self.player:   #if pawn on the grid is from the same player they are going to be after each other
                        if self.goingToHouse == False:
                            break
                        else:
                            self.positionRow = previousPositionRow
                            self.positionColumn = previousPositionColumn
                            locationOfPawns.board[self.positionRow][self.positionColumn] = self
                            return False #it is not possible to move to house
                    else:
                        grid.returnToYard(locationOfPawns)


           go()
           if self.goingToHouse == True:
                   movesToHouse += 1
                   if movesToHouse + self.gridInHouse > locationOfPawns.sizeOfHouse:
                    self.positionRow = previousPositionRow
                    self.positionColumn = previousPositionColumn
                    locationOfPawns.board[self.positionRow][self.positionColumn] = self
                    return False #it is not possible to move to house


        if self.goingToHouse == True:
                self.gridInHouse += movesToHouse
                
                
        
        #setting a pawn to a certain location
        locationOfPawns.board[self.positionRow][self.positionColumn] = self
        return locationOfPawns


    #setting pawn on the start place
    def setOnStart(self, locationOfPawns):
        

        if self.player == 1:
            #position of the start place
            nextPositionRow = locationOfPawns.sizeOfYard
            nextPositionColumn = 0
        
        if self.player == 2:
            #position of the start place
            nextPositionRow = 0
            nextPositionColumn = locationOfPawns.sizeOfYard + 2
        
        if self.player == 3:
            #position of the start place
            nextPositionRow = locationOfPawns.sizeOfYard + 2
            nextPositionColumn = locationOfPawns.sizeBoard - 1

        if self.player == 4:
            #position of the start place
            nextPositionRow = locationOfPawns.sizeBoard - 1
            nextPositionColumn = locationOfPawns.sizeOfYard

                       
        if  locationOfPawns.board[nextPositionRow][nextPositionColumn] == 0: #if start is empty
            locationOfPawns.board[self.positionRow][self.positionColumn] = 0
            self.positionRow = nextPositionRow
            self.positionColumn = nextPositionColumn
            locationOfPawns.board[self.positionRow][self.positionColumn] = self
            return True
        return False


    def returnToYard(self, locationOfPawns): #TODO
        locationOfPawns.board[self.positionRow][self.positionColumn] = 0
        
        if self.player == 1:
            # coordinate of place for pawn top left
            placeForPawnRow = 0 + 2
            placeForPawnColumn = 0 + 2

        if self.player == 2:
            # coordinate of place for pawn top left
            placeForPawnRow = 0 + 2
            placeForPawnColumn = locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2

        if self.player == 3:
            # coordinate of place for pawn top left
            placeForPawnRow = locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2
            placeForPawnColumn = locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2

        if self.player == 4:
            # coordinate of place for pawn top left
            placeForPawnRow = locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2
            placeForPawnColumn = 0 + 2
     
        for i in range (0, 3, 2):
            for j in range(0, 3, 2):
                if locationOfPawns.board[placeForPawnRow + i][placeForPawnColumn + j] == 0:
                    
                    self.positionRow = placeForPawnRow + i
                    self.positionColumn = placeForPawnColumn + j
                    locationOfPawns.board[self.positionRow][self.positionColumn] = self

                    return

        return locationOfPawns

class Board:
    def __init__(self):
        self.sizeBoard = 17
        self.board = [[0] * self.sizeBoard for _ in range(self.sizeBoard)]
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
        
        self.board[self.sizeOfYard][0] = 1  #setting starting grid for player 1
        self.board[0][self.sizeOfYard + 2] = 2  #setting starting grid for player 2
        self.board[self.sizeOfYard + 2][self.sizeBoard - 1] = 3  #setting starting grid for player 3
        self.board[self.sizeBoard - 1][self.sizeOfYard] = 4  #setting starting grid for player 4
          
    #creates a board with yards and houses
    def createBoard(self):
        self.setHouses()
        self.setYards()
        self.setStarts()

    def printingBoard(self):    #TODO
        for i in range(self.sizeBoard):
            s =''
            for j in range(self.sizeBoard):
                if isinstance(self.board[i][j], Pawn):
                    s += str(self.board[i][j].name) + ' '
                else:
                    s += str(self.board[i][j]) + ' '
            print(s)
        print(' ')

class Player:
    def __init__(self, number, identificator, bot):
        self.pawns = []
        self.identificator = identificator
        self.number = number
        self.bot = bot

    def setPawns(self, yardRow, yardColumn, locationOfPawns):
        #setting four pawns
        count = 0
        for i in range (0, 3, 2):
            for j in range (0, 3, 2):
                count += 1
                pawn = Pawn(yardRow + i, yardColumn + j, self.number, self.identificator + str(count))
                self.pawns.append(pawn)
                locationOfPawns.board[yardRow + i][yardColumn + j] = pawn #putting it on the board with pawns
    
    def isWinner(self):
        
        for pawn in self.pawns:
            if pawn.gridInHouse == 0:
                return False
        len(self.pawns)
        return True


    
class Game:
    def __init__(self):
        self.boardPawns = Board()
        self.turn = 1
        self.numberOfPlayers = 1
        self.players = []
        self.rolledNumber = -1
        self.numberOfBots = 0
        
    #creates players for the game
    def settingPlayers(self):
        self.players.append(Player(1, 'G', False))
        self.players.append(Player(2, 'R', False))
        self.players.append(Player(3, 'B', False))
        self.players.append(Player(4, 'Y', False))

    def settingBots(self):
        for i in range(self.numberOfBots):
            self.players[i].bot = True


    def settingPawns(self, locationOfPawns):
        self.settingPlayers()
        self.settingBots()

        for i in range(4):
            assert isinstance(self.players[i], Player), 'it is not a player'

        self.players[0].setPawns(0 + 2, 0 + 2, locationOfPawns)
        self.players[1].setPawns(0 + 2, locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2, locationOfPawns)
        self.players[2].setPawns(locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2, locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2, locationOfPawns)
        self.players[3].setPawns(locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2, 0 + 2, locationOfPawns)
                      
    def setNumberOfPlayers(self):
        print('type number of players from 2 to 4')
        self.numberOfPlayers = int(input())
        while self.numberOfPlayers < 2 or self.numberOfPlayers > 4:
            print('wrong number please type again')
            self.numberOfPlayers = int(input())


    def setNumberOfBots(self):
        print('type number of bots from 0 to 4')
        self.numberOfBots = int(input())
        while self.numberOfBots < 0 or self.numberOfBots > 4:
            print('wrong number please type again')
            self.numberOfBots = int(input())

        
       
       
    #sets a new pawn on the starting point of the playing player and returns True
    # if it is not possible returns False
    def newPawn(self, locationOfPawns):

        #checks if there is a pawn in the yard and if it is sets it on the start and returns True
        # if it is not returns False 
        def checkingYard(yardRow, yardColumn, locationOfPawns):
            for i in range (0, 3, 2):
                for j in range (0, 3, 2):
                    grid = locationOfPawns.board[yardRow + i][yardColumn + j]
                    if isinstance(grid, Pawn):
                        if (grid.setOnStart(locationOfPawns)):
                            return True
                        else:
                            return False
                    
            return False

        if self.turn == 1:
            return checkingYard(0 + 2, 0 + 2, locationOfPawns)

        if self.turn == 2:
            return checkingYard(0 + 2, locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2, locationOfPawns)

        if self.turn == 3:
            return checkingYard(locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2, locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2, locationOfPawns)

        if self.turn == 4:
              return checkingYard(locationOfPawns.sizeBoard - locationOfPawns.sizeOfYard + 2, 0 + 2, locationOfPawns)
        
        
    #decisions made if a player is a bot 
    def actingBot(self):
        def movingPawn():
            for pawn in self.players[self.turn - 1].pawns:
                   if pawn.move(self.rolledNumber, self.boardPawns) == True:
                       break

        if self.players[self.turn - 1].bot ==True:
            print('bot is playing')
            if self.rollingDice() == 6:
                if self.newPawn(self.boardPawns) == False:
                    movingPawn()
               
                    

    def isOver(self):
        for player in self.players:
            assert isinstance(player, Player), 'it is not a player'
            if player.isWinner():
                return True
        return False

    
    #it sets a new pawn to a player and returns True if possible False if not, it has messages for a player
    def givingNewPawn(self): #TODO
        if self.newPawn(self.boardPawns) == False:
            return False
        else:
            print('new pawn is ready')
            return True

    #moves a certain pawn a number of moves return True if possible and False if not it also has messages for a player
    def movingPawn(self, numberOfMoves): #TODO
        print('What pawn do you want to move?')
        namePawn = input()

        for pawn in self.players[self.turn - 1].pawns:
            if pawn.name == namePawn:
                p = pawn
            else:
                print('pawn not found')
                return False

        
        
        if p.move(numberOfMoves, self.boardPawns) == False:
            return False
        else:
            print('pawn moved')
            return True
        print('moving pawn')




    #switch to the next Player
    def switchPlayer(self):
        
        self.turn += 1
        if self.turn > self.numberOfPlayers:
            self.turn = 1

    def  getRolledNumber(self):
             return self.rolledNumber
        #rolling a dice
    def rollingDice(self):
        print('Rolling a dice ...')
        self.rolledNumber = random.randint(1, 6)
        print('Number rolled is:', self.rolledNumber)

    def rollingDiceProcess(self):
        actionCorrect = False
        #print message of options you have when you roll 6
        def printOptionsMessage():
            print('type NEW if you want a new pawn and or type MOVE if you want to move a pawn')
       
        self.rollingDice()

        if self.rolledNumber == 6:   #if 6 is rolled
            printOptionsMessage() 
            choice = input()    #choice of a player
            while choice != 'NEW' and choice != 'MOVE'and actionCorrect == False: #testing validity
                print('Invalid option type it again')
                printOptionsMessage()
                choice = input()
            
            if choice == 'NEW':
                if self.givingNewPawn() == True:  
                    actionCorrect = True
                else:
                    print('I cannot give you a new pawn')
            if choice == 'MOVE':
                if self.movingPawn(self.rolledNumber) == True:
                    actionCorrect == True
                else:
                    print('I cannot move the pawn')
        else:
            if self.movingPawn(self.rolledNumber) == True:
                actionCorrect == True
            else:
                print('I cannot move the pawn')         


    def printPlayer(self):
        print('it is turn of player', self.turn )
    

    def displayingGameBoard(self):
        #colors used
        # green = "\033[1;32;40m"
        # yellow = "\033[1;33;40m"
        # red = "\033[1;31;40m"
        # blue = "\033[1;34;40m"
        # white = "\033[1;37;40m"

        colors = ["\033[1;37;40m", "\033[1;32;40m", "\033[1;31;40m", "\033[1;34;40m", "\033[1;33;40m"]

        colorfulBoard = Board()
        colorfulBoard.createBoard()

        for row in range (colorfulBoard.sizeBoard):
            s1 = []
            s2 = []
            s3 = []
            
            for col in range(colorfulBoard.sizeBoard):
                colorOfBoard = colors[colorfulBoard.board[row][col]] #coloring board
                grid = self.boardPawns.board[row][col]

                boardLR = colorOfBoard + ' |' #colorful string for making left and right sides of a grid
                boardUD = colorOfBoard + ' -----' #colorful string for making top and botom sides of a grid
                if isinstance(grid, Pawn):
                    colorOfPawn = colors[grid.player] #coloring pawns
                    stringForPawn = colorOfPawn + grid.name
                else:
                     stringForPawn = '  '
                s1.append("")
                s1.append(boardUD,)
                s1.append("")

                s2.append(boardLR) 
                s2.append(stringForPawn)
                s2.append(boardLR)
               
                s3.append("")
                s3.append(boardUD)
                s3.append("")

            print(*s1)
            print(*s2)
            print(*s3)



       #put colors to white for writing
        print(colors[0])


def play():
    game = Game()

    #setting the game
    
    game.setNumberOfPlayers()
    game.setNumberOfBots()
    game.settingPawns(game.boardPawns)
    game.displayingGameBoard()

    agreeingToContinue = ''   #if the game should continue




    while(game.isOver() == False and agreeingToContinue != 'NO'):
        game.printPlayer()

        if game.players[game.turn - 1].bot == True:
            game.actingBot()
        else:
             game.rollingDiceProcess()    
       
        game.displayingGameBoard()
        game.switchPlayer()


        print('Do you want to continue? if you want to quit type NO')
        agreeingToContinue = input()
    
    
    print('Game is over')


play()



