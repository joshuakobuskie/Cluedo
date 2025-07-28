from JoshuaKobuskie_Gameboard import CluedoBoard
from JoshuaKobuskie_Player import Player
import os
import time

def main():

    os.system("cls" if os.name == "nt" else "clear")

    board = CluedoBoard()

    print("Welcome to Cluedo!")
    player_count = ""
    while type(player_count) != int:
        try:
            player_count = input("Please enter the number of players between 1 and 5: ")
            player_count = int(player_count)
            if player_count < 1 or player_count > 5:
                print("Invalid selection: Please enter a value between 1 and 5")
                player_count = ""
        except ValueError:
            print("Invalid selection: Please enter a value between 1 and 5")
    
    # Last player will be an AI
    board.setup(player_count+1)

    print("The game is about to begin! Please pass the device to Player 1.")
    time.sleep(5)

    while board.get_play():
        current_player = board.get_current_player()
        current_player.move(board)
        os.system("cls" if os.name == "nt" else "clear")
        board.next_player()
        current_player = board.get_current_player()
        if current_player.get_AI():
            print("Your turn is over. It is now Player {}'s (AI) turn.".format(current_player.get_player_number()))
        else:
            print("Your turn is over. Please pass the device to Player {}.".format(current_player.get_player_number()))
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
