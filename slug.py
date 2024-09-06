from kivy.uix.accordion import NumericProperty
from kivy.uix.accordion import StringProperty
from kivy.uix.behaviors.touchripple import RelativeLayout

class Slug(RelativeLayout):
    body_image = StringProperty('')
    eye_image = StringProperty('')
    y_position = NumericProperty(0)
    