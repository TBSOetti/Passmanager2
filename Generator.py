import secrets
import string

class PasswordGenerator:
    def generate_password(self):
        length = secrets.choice(range(50, 101))  # zufällige Länge zwischen 12 und 16
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password
