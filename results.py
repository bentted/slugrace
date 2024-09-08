from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.accordion import NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen
class Result(BoxLayout):
    player_name = StringProperty('')
    money_before = NumericProperty(0)
    bet_amount = NumericProperty(0)
    slug_name = StringProperty('')
    result_info = StringProperty('')
    gain_or_loss = NumericProperty(0)
    current_money = NumericProperty(0)
    odds = StringProperty('')

class ResultsScreen(Screen):
    pass

class ResultsApp(App):
    def build(self):
        return ResultsScreen()

