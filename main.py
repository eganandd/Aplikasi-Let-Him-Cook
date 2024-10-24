from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Load kv files
Builder.load_file(r'kv/home.kv')       # Home screen
Builder.load_file(r'kv/login.kv')      # Login screen
Builder.load_file(r'kv/daftar.kv')     # Register screen
Builder.load_file(r'kv/beranda.kv')    # Beranda screen
Builder.load_file(r'kv/artikel.kv')    # Artikel screen
Builder.load_file(r'kv/resep.kv')      # Resep screen
Builder.load_file(r'kv/profil.kv')     # Profil screen
Builder.load_file(r'kv/resep1.kv')     # Resep1 screen
Builder.load_file(r'kv/artikel1.kv')   # Artikel1 screen

# Define the screens
class HomeScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class BerandaScreen(Screen):
    pass

class ArtikelScreen(Screen):
    pass

class ResepScreen(Screen):
    pass

class ProfilScreen(Screen):
    pass

class Resep1Screen(Screen):  # Detailed recipe screen for a specific recipe
    pass

class Artikel1Screen(Screen):  # Detailed article screen for a specific article
    pass

class KeluarScreen(Screen):  # Exit confirmation screen
    def __init__(self, **kwargs):
        super(KeluarScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        label = Label(text="Apakah Anda yakin ingin keluar?", font_size=20)
        layout.add_widget(label)

        # Button for confirming exit
        exit_button = Button(text="Ya, Keluar", background_color=(0.8, 0.3, 0.3, 1))
        exit_button.bind(on_release=self.exit_app)
        layout.add_widget(exit_button)

        # Button for canceling
        cancel_button = Button(text="Batal", background_color=(0.3, 0.6, 0.3, 1))
        cancel_button.bind(on_release=self.cancel_exit)
        layout.add_widget(cancel_button)

        self.add_widget(layout)

    def exit_app(self, instance):
        App.get_running_app().stop()  # Exits the application

    def cancel_exit(self, instance):
        self.manager.current = 'profil'  # Navigates back to the Profil screen

# Custom ScreenManager
class MyScreenManager(ScreenManager):
    pass

# Main App
class MyApp(App):
    def build(self):
        # Create an instance of the ScreenManager
        sm = MyScreenManager()

        # Add screens to the ScreenManager
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoginScreen(name="masuk"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(BerandaScreen(name="beranda"))
        sm.add_widget(ArtikelScreen(name="artikel"))
        sm.add_widget(ResepScreen(name="resep"))
        sm.add_widget(ProfilScreen(name="profil"))
        sm.add_widget(Resep1Screen(name="resep1"))  # Add the detailed recipe screen
        sm.add_widget(Artikel1Screen(name="artikel1"))  # Add detailed article screen
        sm.add_widget(KeluarScreen(name='keluar'))  # Add the exit confirmation screen

        return sm

    # Function to navigate to specific recipe screens
    def show_recipe(self, recipe_name):
        self.root.current = recipe_name  # Navigate directly to the specified recipe screen

    # Function to navigate to specific article screens
    def show_article(self, article_name):
        self.root.current = article_name  # Navigate directly to the specified article screen

if __name__ == '__main__':
    MyApp().run()
