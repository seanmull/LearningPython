class Game(object):

    def __init__(self):
        self.board = list(range(1,10))
        self.currentPlayer = 'X'

    def checkIfValidLoc(self,loc):
        inBounds = loc >= 1 and loc <= 9
        return inBounds and self.board[loc - 1] != 'O' \
               and self.board[loc - 1] != 'X' 
    
    def enterXorO(self, XorO):
        loc = 99
        while not self.checkIfValidLoc(loc): 
            loc = int(input("Enter in what location you want to put your mark:"))
        self.board[loc - 1] = XorO

    def checkWinCondition(self, XorO):
        winConditions = [(0,1,2), (3,4,5), (6,7,8), \
                         (0,3,6),(1,4,7),(2,5,8), \
                         (0,4,8),(2,4,6)]

        for condition in winConditions:
            count = 0
            for loc in condition:
                if self.board[loc] == XorO:
                    count += 1
            if count == 3:
                self.displayWinner(XorO)

    def displayCurrentLocations(self):
        print("Print current locations taken by X or O:")
        for pos in enumerate(self.board):
            if pos[1] == 'O' or pos[1] == 'X':
                loc = pos[1]
            else:
                loc = pos[0] + 1
            print(loc, end='')
            print(" ", end='')
            if (pos[0] + 1) % 3 == 0:
                print()

    def displayWinner(self, XorO):
        print(XorO,"is the winner!")
        exit()

    def switchPlayer(self):
        if self.currentPlayer == 'X':
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'

def main():
    game = Game()
    while True:
        player = game.currentPlayer
        game.displayCurrentLocations()
        game.enterXorO(player)
        game.checkWinCondition(player)  
        game.switchPlayer()

if __name__ == "__main__":
    main()
