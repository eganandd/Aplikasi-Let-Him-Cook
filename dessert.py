from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

class DessertScreen(Screen):
    def __init__(self, **kwargs):
        super(DessertScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Add any other widgets or layouts needed here

        self.add_widget(layout)