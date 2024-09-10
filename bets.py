from kivy.uix.boxlayout import BoxLayout
from kivy.uix.accordion import NumericProperty, StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen

class Bet(BoxLayout):
    player_name = StringProperty('')
    bet_amount = NumericProperty(0)
    max_bet_amount = NumericProperty(0)
    player_group = StringProperty('')
    selected_slug = NumericProperty(0)

    def update_player_bet(self, player):
        player.bet = self.bet_amount

class BetsScreen(Screen):
    all_slugs_selected = BooleanProperty(False)

    def select_slug(self, player, slug_index):
        if slug_index >=0:
            # Set the player's chosen_slug to the slug with the index passed as an argument.
            player.chosen_slug = self.game.slugs[slug_index]

            # Create a list of players who have chosen a slug.
            players_with_slugs = [player for player in self.game.players
                                if player.chosen_slug]

        # Compare the list of players with slugs with the list of all players in
        # the game and assign the result of this comparison to the BooleanProperty
        # all_slugs_selected.
        self.all_slugs_selected = len(players_with_slugs) == len(self.game.players)
    def clear_bets(self):
        self.all_slugs_selected = False
        for bet in self.bets:
            for slug_button in bet.slug_buttons:
                if slug_button.active:
                    slug_button.active = False

