from kivy.uix.actionbar import BoxLayout
from kivy.app import App

class SettingsApp(App):
    def build(self):
        return BoxLayout()
if __name__=='__main__':
    SettingsApp().run()