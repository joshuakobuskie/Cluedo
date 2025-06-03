from JoshuaKobuskie_Gameboard import CluedoBoard
from JoshuaKobuskie_Player import Player
import os
import time

def main():
    # board = CluedoBoard()
    # board.print_board()
    # print(board.check_moves([17, 12]))
    # print(board.check_moves([18, 6]))
    # print(board.check_moves([19, 6]))
    # print(board.check_moves("Hall"))
    # print(board.check_moves("Ballroom"))
    # print(board.check_moves("Kitchen"))

    players = [Player("Miss Scarlett", [])]
    player2 = Player("Mrs. White", [])
    # player2.position = [17, 11]
    players.append(player2)
    board = CluedoBoard()
    print(board.check_moves(players[1], players))
    board.print_board(players)

    

if __name__ == "__main__":
    main()

    # This is going to move into a while loop in main later
    # Use to clear screen between turns
    os.system("cls" if os.name == "nt" else "clear")
    print("Your turn is over! Please pass the device to the next player")
    time.sleep(5)
    os.system("cls" if os.name == "nt" else "clear")

    main()
