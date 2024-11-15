from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from auth import AuthService  
from dessert import DessertScreen  
from masakan_tradisional import MasakanTradisionalScreen
from resep_ayam import ResepAyamScreen
from resep_daging import ResepDagingScreen
from favorit import FavoritScreen

auth_service = AuthService()

# Load kv files for screens
for kv_file in [
    'home.kv', 'login.kv', 'daftar.kv', 'beranda.kv', 'artikel.kv', 
    'resep.kv', 'profil.kv', 'resep1.kv', 'resep2.kv', 'artikel1.kv', 
    'artikel2.kv', 'artikel3.kv', 'dessert.kv', 'masakan_tradisional.kv', 'resep_ayam.kv', 'resep_daging.kv', 'favorit.kv'
]:
    Builder.load_file(f'kv/{kv_file}')

# Define screens
class HomeScreen(Screen):
    pass

class LoginScreen(Screen):
    def login(self, email, password):
        success, message = auth_service.login(email, password)
        
        if success:
            app = App.get_running_app()
            if app.user_role == 'pengguna':
                app.root.current = 'beranda'
            else:
                self.show_popup('Error', f"Role '{app.user_role}' not recognized")
        else:
            self.show_popup('Login Failed', message)

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

class DaftarScreen(Screen):
    def daftar(self, username, email, password):
        success, message = auth_service.daftar(username, email, password)
        if success:
            App.get_running_app().root.current = 'login'
        else:
            self.show_popup('Registration Failed', message)

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

class BerandaScreen(Screen):
    pass

class ArtikelScreen(Screen):
    pass

class ResepScreen(Screen):
    pass

class ProfilScreen(Screen):
    pass

class Resep1Screen(Screen):
    pass

class Resep2Screen(Screen):  
    pass

class Artikel1Screen(Screen):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):  # Checks if touch is within the widget
            app = App.get_running_app()
            app.show_recipe('resep1')  # Navigate to Resep1Screen
        return super().on_touch_down(touch)

class Artikel2Screen(Screen):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):  # Checks if touch is within the widget
            app = App.get_running_app()
            app.show_recipe('resep2')  # Navigate to Resep2Screen
        return super().on_touch_down(touch)

class Artikel3Screen(Screen):
    pass

class KeluarScreen(Screen):
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
    user_role = None

    def build(self):
        sm = MyScreenManager()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DaftarScreen(name="daftar"))
        sm.add_widget(BerandaScreen(name="beranda"))
        sm.add_widget(ArtikelScreen(name="artikel"))
        sm.add_widget(ResepScreen(name="resep"))
        sm.add_widget(ProfilScreen(name="profil"))
        sm.add_widget(Resep1Screen(name="resep1"))
        sm.add_widget(Resep2Screen(name="resep2"))  
        sm.add_widget(Artikel1Screen(name="artikel1"))
        sm.add_widget(Artikel2Screen(name="artikel2"))
        sm.add_widget(Artikel3Screen(name="artikel3"))
        sm.add_widget(KeluarScreen(name='keluar'))
        sm.add_widget(DessertScreen(name='dessert'))
        sm.add_widget(MasakanTradisionalScreen(name='masakan_tradisional'))
        sm.add_widget(ResepAyamScreen(name='resep_ayam'))
        sm.add_widget(ResepDagingScreen(name='resep_daging'))
        sm.add_widget(FavoritScreen(name='favorit'))
        
        return sm
    
    def show_category(self, category_name):
        if category_name == 'dessert':
            self.root.current = 'dessert'
        
        if category_name == 'masakan_tradisional':
            self.root.current = 'masakan_tradisional'
        
        if category_name == 'resep_ayam':
            self.root.current = 'resep_ayam'
        
        if category_name == 'resep_daging':
            self.root.current = 'resep_daging'
    
    def show_recipe(self, recipe_name):
        # Navigate to the specific recipe screen based on recipe_name
        self.root.current = recipe_name  # Example: 'resep1' will navigate to Resep1Screen

if __name__ == '__main__':
    MyApp().run()
