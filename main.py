from Mastermanager import MasterKeyManager
from Manager import PasswordManager
from Generator import PasswordGenerator

def main():
    mastersafe = MasterKeyManager('master.json')
    generator = PasswordGenerator()

    if not mastersafe.master_key_exists():
        print("Kein Master-Key gefunden. Bitte legen Sie einen fest.")
        mastersafe.set_master_key()

    while True:
        master_key_input = input("Bitte geben Sie den Master-Key ein: ")
        if mastersafe.verify_master_key(master_key_input):
            print("Master-Key verifiziert.\n")
            safefile = PasswordManager('password.json')
            break
        else:
            print("Ungültiger Master-Key. Bitte versuchen Sie es erneut.\n")

    while True:
        print("1. Passwort hinzufügen")
        print("2. Passwort anzeigen")
        print("3. Passwort löschen")
        print("4. Beenden")
        choice = input("Wähle eine Option: ")

        if choice == '1':
            username = input("Benutzername: ")
            use_generated = input("Möchten Sie ein zufälliges Passwort generieren lassen? (j/n): ")
            if use_generated.lower() == 'j':
                password = generator.generate_password()  # Verwende den Generator
                print(f"Generiertes Passwort: {password}")
            else:
                password = input("Passwort: ")
            safefile.add_password(username, password)  # Speichere im Klartext
            print("Passwort hinzugefügt\n")
        elif choice == '2':
            username = input("Benutzername: ")
            password = safefile.get_password(username)
            if password:
                print(f"Passwort für {username}: {password}\n")
            else:
                print("Benutzername nicht gefunden.\n")
        elif choice == '3':
            username = input("Benutzername: ")
            confirm = input(f"Sind Sie sicher, dass Sie das Passwort für den Benutzer {username} löschen möchten? j/n: ")
            if confirm.lower() == 'j':
                safefile.delete_password(username)
                print("Passwort gelöscht.\n")
            else:
                print("Passwort wurde nicht gelöscht\n")
        elif choice == '4':
            break
        else:
            print("Ungültige Option\n")

if __name__ == '__main__':
    main()
