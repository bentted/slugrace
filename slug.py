from kivy.uix.accordion import NumericProperty
from kivy.uix.accordion import StringProperty
from kivy.uix.behaviors.touchripple import RelativeLayout

class Slug(RelativeLayout):
    name = StringProperty('')
    body_image = StringProperty('')
    eye_image = StringProperty('')
    front_image = StringProperty('')
    y_position = NumericProperty(0)

    wins = NumericProperty(0)

    win_percent = NumericProperty(0)

    odds = NumericProperty(0)
    def update(self, winning_slug):
        if self == winning_slug:
            self.odds = round(max(1.01, min(self.odds *.96,20)),2)
        else:
            self.odds = round(max(1.01, min(self.odds + 1.03, 20)),2)
    