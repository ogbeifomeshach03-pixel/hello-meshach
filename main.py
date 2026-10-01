from kivy.app import App
from kivy.uix.button import Button


class MeshachApp(App):

    def build(self):
        return Button(
            text="Hello Meshach!",
            font_size=30
        )


MeshachApp().run()