from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class FavoritScreen(Screen):
    def on_enter(self):
        # Saat masuk ke layar ini, bisa muat daftar favorit dari sumber data
        # Misalnya, panggil fungsi yang mengambil data favorit
        self.load_favorites()

    def load_favorites(self):
        # Contoh statis data favorit; bisa diganti dengan data dinamis
        favorites = [
            "Nasi Goreng Rempah",
            "Mango Sago",
            "Chocolate Cake"
        ]
        
        # Hapus widget sebelumnya untuk memperbarui daftar favorit
        self.ids.favorites_box.clear_widgets()

        # Tampilkan setiap item favorit dalam layout
        for item in favorites:
            label = Label(
                text=item,
                font_size=18,
                color=(0.3, 0.3, 0.3, 1),
                size_hint_y=None,
                height=40
            )
            self.ids.favorites_box.add_widget(label)
