from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.app import App
from auth import AuthService

auth_service = AuthService()

class ProfilScreen(Screen):
    def on_enter(self):
        # This method is called every time the screen is entered
        self.display_user_info()

    def display_user_info(self):
        # Clear any previous widgets from layout
        self.clear_widgets()

        # Fetch user data (assuming `user_role` and `user_email` are stored in the app instance)
        app = App.get_running_app()
        user_role = getattr(app, 'user_role', 'N/A')  # Defaults to 'N/A' if not set
        user_email = getattr(app, 'user_email', 'N/A')  # Defaults to 'N/A' if not set

        # Check if layout already exists in case of repeated calls
        if not self.children:
            # Main layout to hold user info and buttons
            layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

            # Display user email and role
            email_label = Label(text=f"Email: {user_email}", font_size=18)
            role_label = Label(text=f"Role: {user_role}", font_size=18)
            layout.add_widget(email_label)
            layout.add_widget(role_label)

            # Add Edit Profile button
            edit_button = Button(text="Edit Profile", size_hint=(None, None), size=(150, 50))
            edit_button.bind(on_release=self.show_edit_profile_popup)
            layout.add_widget(edit_button)

            # Add Logout button
            logout_button = Button(text="Logout", background_color=(0.8, 0.3, 0.3, 1), size_hint=(None, None), size=(150, 50))
            logout_button.bind(on_release=self.logout)
            layout.add_widget(logout_button)

            # Add layout to the screen
            self.add_widget(layout)

    def show_edit_profile_popup(self, instance):
        # Popup to simulate edit profile
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text="Feature Coming Soon!", font_size=18))

        close_button = Button(text="Close", size_hint=(None, None), size=(100, 50))
        close_button.bind(on_release=lambda x: popup.dismiss())
        layout.add_widget(close_button)

        popup = Popup(title="Edit Profile", content=layout, size_hint=(None, None), size=(400, 200))
        popup.open()

    def logout(self, instance):
        # Clear user data and navigate to the login screen
        app = App.get_running_app()
        app.user_role = None
        app.user_email = None
        app.root.current = 'login'
