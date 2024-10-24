from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class ArtikelScreen(Screen):
    def __init__(self, **kwargs):
        super(ArtikelScreen, self).__init__(**kwargs)

# Load the kv file
Builder.load_file('artikel.kv')
