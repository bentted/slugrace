from kivy.uix.behaviors.codenavigation import EventDispatcher
from kivy.uix.accordion import StringProperty, NumericProperty

class Player(EventDispatcher):
    name= StringProperty('')
    initial_money = NumericProperty(0)
    money = NumericProperty(0)
    money_before_race = NumericProperty(0)
    money_won = NumericProperty(0)
    bet = NumericProperty(1)