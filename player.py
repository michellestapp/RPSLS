

class Player:
    def __init__(self) -> None:
        self.player_one = ()
        self.player_two = ()
    
    def choosing_the_players(self):
        self.number_of_players = input(f'choose the number of players from 0-2')
        if self.number_of_players == '0':
            self.player_one = ai_player_random 
            self.player_two = ai_player_random
        elif self.number_of_players == "1":
            self.player_one = human_player
            self.player_two = ai_player_random
        elif self.number_of_players == "2":
            self.player_one = human_player
            self.player_two = human_player
    
    
