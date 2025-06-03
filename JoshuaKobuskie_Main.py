from JoshuaKobuskie_Gameboard import CluedoBoard
from JoshuaKobuskie_Player import Player

def main():
    # board = CluedoBoard()
    # board.print_board()
    # print(board.check_moves([17, 12]))
    # print(board.check_moves([18, 6]))
    # print(board.check_moves([19, 6]))
    # print(board.check_moves("Hall"))
    # print(board.check_moves("Ballroom"))
    # print(board.check_moves("Kitchen"))

    players = [Player("Miss Scarlett")]
    board = CluedoBoard()
    board.print_board(players)

if __name__ == "__main__":
    main()