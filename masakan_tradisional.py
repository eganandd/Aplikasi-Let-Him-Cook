from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# Load the KV file associated with MasakanTradisionalScreen
Builder.load_file('kv/masakan_tradisional.kv')

class MasakanTradisionalScreen(Screen):
    pass  # Semua elemen UI dan tata letak didefinisikan di dalam file KV
