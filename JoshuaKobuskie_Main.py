from JoshuaKobuskie_Gameboard import CluedoBoard
from JoshuaKobuskie_Player import Player
import os
import time

def main():

    # FOR TESTING USE ONLY
    # board = CluedoBoard()
    # board.print_board()
    # print(board.check_moves([17, 12]))
    # print(board.check_moves([18, 6]))
    # print(board.check_moves([19, 6]))
    # print(board.check_moves("Hall"))
    # print(board.check_moves("Ballroom"))
    # print(board.check_moves("Kitchen"))

    # players = [Player("Miss Scarlett", [])]
    # players[0].position = [17,11]
    # player2 = Player("Mrs. White", [])
    # player2.position = "Hall"
    # players.append(player2)
    # board = CluedoBoard()
    # print(board.check_moves(players[1], players))
    # board.print_board(players)

    # REAL CODE STARTS HERE
    board = CluedoBoard()

    print("Welcome to Cluedo!")
    player_count = ""
    while type(player_count) != int:
        try:
            player_count = input("Please enter the number of players: ")
            player_count = int(player_count)
            if player_count < 1 or player_count > 6:
                print("Invalid selection: Please enter a value between 1 and 6")
                player_count = ""
        except ValueError:
            print("Invalid selection: Please enter a value between 1 and 6")
    
    players = board.setup(player_count)

    print("The game is about to begin! Please pass the device to Player 1!")
    time.sleep(5)
    os.system("cls" if os.name == "nt" else "clear")
    board.print_board()
    board.get_player_info()
    board.players[0].move(board)

if __name__ == "__main__":
    main()

    # This is going to move into a while loop in main later
    # Use to clear screen between turns
    # os.system("cls" if os.name == "nt" else "clear")
    # print("Your turn is over! Please pass the device to the next player")
    # time.sleep(5)
    # os.system("cls" if os.name == "nt" else "clear")

    # main()
