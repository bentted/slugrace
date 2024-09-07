from kivy.uix.accordion import NumericProperty
from kivy.uix.textinput import TextInput
from kivy.app import App


class NameInput(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    def insert_text(self, substring, from_undo=False):
        if len(self.text+substring) <= self.app.max_name_length:
            return super(NameInput, self).insert_text(substring, from_undo = from_undo)
class NumInput(TextInput):
    min_value = NumericProperty()
    max_value = NumericProperty()
    def insert_text(self, substring, from_undo = False):
        return(super().insert_text(substring, from_undo=from_undo) if substring !='-'
               else super().insert_text('', from_undo=from_undo))
    def on_text_validate(self):
        if self.text:
            self.text = str(max(self.min_value, min(int(self.text), self.max_value)))
    def on_focus(self, instance, value):
        if not value:
            self.on_text_validate()
    