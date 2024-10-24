from kivy.uix.screenmanager import Screen

class KeluarScreen(Screen):
    def confirm_exit(self):
        # Logic to exit the app or return to the login screen can be added here
        # For example, you can call a method to log the user out
        print("User has logged out")
        # Here you could switch back to the login screen or close the app if needed
        self.manager.current = 'login'  # Adjust as per your screen management
