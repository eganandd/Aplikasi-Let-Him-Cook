import pyrebase
from kivy.app import App
from config import get_firebase_config

# Firebase configuration
config = get_firebase_config()
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

class AuthService:
    def login(self, email, password):
        try:
            # Attempt to sign in the user
            user = auth.sign_in_with_email_and_password(email, password)
            user_id = user['localId']

            # Retrieve the user's role directly from Firebase
            role = db.child("users").child(user_id).child("role").get().val()
            
            if role:
                # Store the role in the app instance for easy access
                App.get_running_app().user_role = role
                return True, "Login successful"
            else:
                return False, "User role not found in database"
        
        except Exception as e:
            error_message = str(e)
            if "EMAIL_NOT_FOUND" in error_message:
                return False, "Email not found. Please check your credentials."
            elif "INVALID_PASSWORD" in error_message:
                return False, "Invalid password. Please try again."
            else:
                return False, f"Login failed: {error_message}"

    def daftar(self, username, email, password, role='pengguna'):
        try:
            # Attempt to create a new user
            user = auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']

            # Save user information in the Firebase Realtime Database
            db.child("users").child(user_id).set({
                "username": username,
                "email": email,
                "role": role
            })
            return True, "Registration successful"
        
        except Exception as e:
            error_message = str(e)
            if "EMAIL_EXISTS" in error_message:
                return False, "Email already in use. Please choose another."
            elif "WEAK_PASSWORD" in error_message:
                return False, "Password is too weak. Please use a stronger password."
            else:
                return False, f"Registration failed: {error_message}"
