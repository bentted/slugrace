from kivy.uix.actionbar import BoxLayout
from kivy.app import App

class SettingsScreen(BoxLayout):
    pass
class SettingsApp(App):
    def build(self):
        return SettingsScreen()
if __name__=='__main__':
    SettingsApp().run()