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
