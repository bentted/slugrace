from kivy.uix.actionbar import BoxLayout
from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')
Config.set('graphics', 'resizable', '0')

class SettingsScreen(BoxLayout):
    pass
class SettingsApp(App):
    def build(self):
        return SettingsScreen()
if __name__=='__main__':
    SettingsApp().run()