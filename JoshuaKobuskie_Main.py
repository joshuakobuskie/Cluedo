from JoshuaKobuskie_Gameboard import CluedoBoard
import os
import time

def main():

    os.system("cls" if os.name == "nt" else "clear")

    board = CluedoBoard()

    print("Welcome to Cluedo!")
    player_count = ""
    ai_count = ""

    # Select number of real players
    while type(player_count) != int:
        try:
            player_count = input("Please enter the number of real players between 1 and 6: ")
            player_count = int(player_count)
            if player_count < 1 or player_count > 6:
                print("Invalid selection: Please enter a value between 1 and 6")
                player_count = ""
        except ValueError:
            print("Invalid selection: Please enter a value between 1 and 6")
    
    # Select number of AI players
    while type(ai_count) != int:
        try:
            ai_count = input("Please enter the number of AI players between 0 and {}: ".format(6-player_count))
            ai_count = int(ai_count)
            if ai_count < 0 or ai_count > (6-player_count):
                print("Invalid selection: Please enter a value between 0 and {}".format(6-player_count))
                ai_count = ""
        except ValueError:
            print("Invalid selection: Please enter a value between 0 and {}".format(6-player_count))

    # Last player will be an AI
    board.setup(player_count, ai_count)

    print("The game is about to begin! Please pass the device to Player 1.")
    time.sleep(3)

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
