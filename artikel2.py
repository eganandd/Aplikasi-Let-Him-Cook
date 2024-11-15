from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

# Load the KV file
Builder.load_file(r'kv/artikel2.kv')

class Artikel1Screen(Screen):  # Detailed article screen for a specific article
    pass

# Main App
class MyApp(App):
    def build(self):
        return Artikel2Screen()

if __name__ == '__main__':
    MyApp().run()
