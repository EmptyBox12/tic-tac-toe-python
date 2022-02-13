class Board:
    def __init__(self):
        self.boardArray = self.create_board()

    def create_board(self):
        array = []
        for i in range(3):
            array.append([])
            for j in range(3):
                array[i].append("-")
        return array

    def place_move(self, x, y, move):
        if(self.boardArray[y][x] == "-"):
            self.boardArray[y][x] = move
            return f"{move} is placed on {x,y}"
        else:
            return "invalid move"
            
    def check_win(self):
        win = False
        for i in range(3):
            if((self.boardArray[i][0] == self.boardArray[i][1] == self.boardArray[i][2]) and self.boardArray[i][0] != "-"):
                win = True
                return win
        for i in range(3):
            if((self.boardArray[0][i] == self.boardArray[1][i] == self.boardArray[2][i]) and self.boardArray[0][i] != "-"):
                win = True
                return win
        if((self.boardArray[0][0] == self.boardArray[1][1] == self.boardArray[2][2]) and self.boardArray[0][1] != "-"):
            win = True
            return win
        if((self.boardArray[0][2] == self.boardArray[1][1] == self.boardArray[2][0]) and self.boardArray[0][2] != "-"):
            win = True
            return win
        return win

    def check_tie(self):
        tie = True
        for i in range(3):
            for j in range(3):
                if(self.boardArray[i][j] == "-"):
                    tie = False
                    return tie
        return tie
    
    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.boardArray[i][j], end=" ")
            print("")