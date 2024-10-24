from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

class BerandaScreen(Screen):
    pass

class BerandaApp(App):
    def build(self):
        return BerandaScreen()

    def show_category(self, category_name):
        # Handle category button press
        print(f"Category {category_name} clicked")

if __name__ == '__main__':
    BerandaApp().run()
