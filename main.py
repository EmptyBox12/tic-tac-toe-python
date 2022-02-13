from Board import Board

gameBoard = Board()
""""
gameBoard.place_move(0,1,"X")
gameBoard.place_move(1,1,"X")
gameBoard.place_move(2,1,"0")

gameBoard.place_move(0,0,"X")
gameBoard.place_move(1,0,"X")
gameBoard.place_move(2,0,"0")

gameBoard.place_move(0,2,"X")
gameBoard.place_move(1,2,"X")
gameBoard.place_move(2,2,"0")
"""

win = gameBoard.check_tie()
gameBoard.print_board()

