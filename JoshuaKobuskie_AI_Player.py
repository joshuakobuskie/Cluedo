from JoshuaKobuskie_Player import Player

class AI_Player(Player):
    def __init__(self, player_number, character, cards, player_count):

        # Create player
        super().__init__(player_number, character, cards)
        
        # Create knowledge base
        # Clue solution is player 0
        self.possible_characters = {"Miss Scarlett":[i for i in range(player_count+1)], "Colonel Mustard":[i for i in range(player_count+1)], "Mrs. White":[i for i in range(player_count+1)], "Reverend Green":[i for i in range(player_count+1)], "Mrs. Peacock":[i for i in range(player_count+1)], "Professor Plum":[i for i in range(player_count+1)]}
        self.possible_weapons = {"Candlestick Holder":[i for i in range(player_count+1)], "Knife":[i for i in range(player_count+1)], "Lead Pipe":[i for i in range(player_count+1)], "Revolver":[i for i in range(player_count+1)], "Rope":[i for i in range(player_count+1)], "Wrench":[i for i in range(player_count+1)]}
        self.possible_rooms = {"Kitchen":[i for i in range(player_count+1)], "Ballroom":[i for i in range(player_count+1)], "Conservatory":[i for i in range(player_count+1)], "Dining Room":[i for i in range(player_count+1)], "Billiard Room":[i for i in range(player_count+1)], "Library":[i for i in range(player_count+1)], "Lounge":[i for i in range(player_count+1)], "Hall":[i for i in range(player_count+1)], "Study":[i for i in range(player_count+1)]}

        # Remove already known cards from the AI knowledge base
        for card in self.cards:
            self.remove_suggestion(self.player_number, card)

        # Remove cards AI knows that it doesnt have
        for character, candidates in self.possible_characters.items():
            if candidates != [self.player_number]:
                self.possible_characters[character].remove(self.player_number)

        for weapon, candidates in self.possible_weapons.items():
            if candidates != [self.player_number]:
                self.possible_weapons[weapon].remove(self.player_number)

        for room, candidates in self.possible_rooms.items():
            if candidates != [self.player_number]:
                self.possible_rooms[room].remove(self.player_number)

    def remove_suggestion(self, disprover, card):
        # Remove players who could not refute a card
        current_player = self.player_number
        while current_player < disprover:
            if card in self.possible_characters:
                self.possible_characters[card].remove(current_player)
            elif card in self.possible_weapons:
                self.possible_weapons[card].remove(current_player)
            elif card in self.possible_rooms:
                self.possible_rooms[card].remove(current_player)
            current_player += 1

        # Update the known card holder
        if card in self.possible_characters:
            self.possible_characters[card] = [disprover]
        elif card in self.possible_weapons:
            self.possible_weapons[card] = [disprover]
        elif card in self.possible_rooms:
            self.possible_rooms[card] = [disprover]

test = AI_Player(2, "Miss Scarlett", ['Mrs. Peacock', 'Candlestick Holder', 'Wrench', 'Kitchen', 'Colonel Mustard', 'Rope', 'Lead Pipe', 'Dining Room', 'Hall'], 2)
print(test.possible_characters)
print(test.possible_weapons)
print(test.possible_rooms)