from Board import Board
from Player import Player


def start_game():
    game_board = Board()
    player1_name = input("First player's name? ")
    player2_name = input("Second player's name? ")

    player1 = Player(player1_name, True, "X")
    player2 = Player(player2_name, False, "O")

    while True:
        while True:
            coordinates = input("Enter x and y coordinates (1 2): ")
            coordinate_list = coordinates.split(" ")
            if(len(coordinate_list)==2 and (coordinate_list[0] != "" and coordinate_list[1] != "") and (int(coordinate_list[0]) >= 0 and (int(coordinate_list[0]) <= 2) and (int(coordinate_list[1]) >= 0 and (int(coordinate_list[1]) <= 2)))):
                if(not game_board.check_occupied(int(coordinate_list[0]), int(coordinate_list[1]))):
                    break

        if(player1.check_turn()):
            place_mark(player1, player2, int(coordinate_list[0]), int(coordinate_list[1]), game_board)
            if(game_board.check_win()):
                print(f"{player1.name} is the winner")
                break
        elif(player2.check_turn()):
            place_mark(player2, player1, int(coordinate_list[0]), int(coordinate_list[1]), game_board)
            if(game_board.check_win()):
                print(f"{player2.name} is the winner")
                break
        if(game_board.check_tie()):
            print("It's a tie")
            break


def place_mark(turn_owner, player, x, y, game_board):
    turn_owner.place_mark(x, y, game_board)
    turn_owner.end_turn()
    player.start_turn()
    game_board.print_board()


start_game()



