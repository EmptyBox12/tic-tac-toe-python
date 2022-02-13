class Player:
    def __init__(self, name, turn, mark):
        self.name = name
        self.turn = turn
        self.mark = mark
    
    def place_mark(self, x, y, board):
        if self.turn:
            board.place_mark(x, y, self.mark)

    def end_turn(self):
        self.turn = False
    
    def start_turn(self):
        self.turn = True

    def check_turn(self):
        return self.turn
    
