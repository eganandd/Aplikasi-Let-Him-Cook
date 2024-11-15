from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/resep_ayam.kv')

class ResepAyamScreen(Screen):
    def on_pre_enter(self):
        # Refresh atau tindakan tambahan jika diperlukan
        pass