from JoshuaKobuskie_Player import Player

class AI_Player(Player):
    def __init__(self, player_number, character, cards, player_count):
        super().__init__(player_number, character, cards)
        self.possible_characters = {"Miss Scarlett":[i+1 for i in range(player_count)], "Colonel Mustard":[i+1 for i in range(player_count)], "Mrs. White":[i+1 for i in range(player_count)], "Reverend Green":[i+1 for i in range(player_count)], "Mrs. Peacock":[i+1 for i in range(player_count)], "Professor Plum":[i+1 for i in range(player_count)]}
        self.possible_weapons = {"Candlestick Holder":[i+1 for i in range(player_count)], "Knife":[i+1 for i in range(player_count)], "Lead Pipe":[i+1 for i in range(player_count)], "Revolver":[i+1 for i in range(player_count)], "Rope":[i+1 for i in range(player_count)], "Wrench":[i+1 for i in range(player_count)]}
        self.possible_rooms = {"Kitchen":[i+1 for i in range(player_count)], "Ballroom":[i+1 for i in range(player_count)], "Conservatory":[i+1 for i in range(player_count)], "Dining Room":[i+1 for i in range(player_count)], "Billiard Room":[i+1 for i in range(player_count)], "Library":[i+1 for i in range(player_count)], "Lounge":[i+1 for i in range(player_count)], "Hall":[i+1 for i in range(player_count)], "Study":[i+1 for i in range(player_count)]}

test = AI_Player(2, "Miss Scarlett", ['Mrs. Peacock', 'Candlestick Holder', 'Wrench', 'Kitchen', 'Colonel Mustard', 'Rope', 'Lead Pipe', 'Dining Room', 'Hall'], 2)
print(test.possible_characters)
print(test.possible_weapons)
print(test.possible_rooms)