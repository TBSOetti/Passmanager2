import json
import os

class PasswordManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.passwords = self.load_passwords()

    def load_passwords(self):
        if not os.path.exists(self.file_path):
            return {}
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Fehler beim Laden der Passwörter: {e}")
            return {}
        except Exception as e:
            print(f"Allgemeiner Fehler beim Laden der Passwörter: {e}")
            return {}

    def save_passwords(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.passwords, file)
        except Exception as e:
            print(f"Fehler beim Speichern der Passwörter: {e}")

    def add_password(self, username, password):
        self.passwords[username] = password  # Speichere das Passwort im Klartext
        self.save_passwords()

    def get_password(self, username):
        return self.passwords.get(username)

    def delete_password(self, username):
        if username in self.passwords:
            del self.passwords[username]
            self.save_passwords()
