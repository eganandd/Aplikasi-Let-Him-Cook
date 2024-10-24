from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

# Load the KV file
Builder.load_file(r'kv/artikel1.kv')

class Artikel1Screen(Screen):  # Detailed article screen for a specific article
    pass

# Main App
class MyApp(App):
    def build(self):
        return Artikel1Screen()

if __name__ == '__main__':
    MyApp().run()
