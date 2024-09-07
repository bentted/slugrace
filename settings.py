from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.accordion import StringProperty
from kivy.uix.screenmanager import Screen


class PlayerCount(BoxLayout):
    count_text = StringProperty('')

class PlayerSettings(BoxLayout):
    label_text = StringProperty('')

class SettingsScreen(Screen):
    def set_players(self, players):
        from kivy.app import App
        app = App.get_running_app()
        for i, player in enumerate(self.game.players):
            player.name = 'Player' + str(i+1) if not players[i].name else players[i].name
            player.initial_money = (1000 if not players[i].player_initial_money 
                                    else max(app.initial_money_min,
                                             min(int(players[i].player_initial_money),app.initial_money_max)))
            player.money = player.initial_money

class SettingsApp(App):
    def build(self):
        return SettingsScreen()
