import json
import os
import bcrypt

class MasterKeyManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.master_key_hash = None
        self.load_master_key()

    def load_master_key(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                try:
                    data = json.load(f)
                    self.master_key_hash = data.get('master_key')
                except json.JSONDecodeError:
                    print("Fehler beim Laden der Master-Key-Datei.")
        else:
            print("Master-Key Datei existiert nicht.")

    def set_master_key(self):
        master_key = input("Bitte geben Sie einen neuen Master-Key ein: ")
        hashed_key = bcrypt.hashpw(master_key.encode('utf-8'), bcrypt.gensalt()).decode()
        self.master_key_hash = hashed_key
        self.save_master_key()
        print("Neuer Master-Key gesetzt.")

    def verify_master_key(self, master_key):
        if self.master_key_hash is None:
            print("Kein Master-Key gespeichert.")
            return False
        return bcrypt.checkpw(master_key.encode('utf-8'), self.master_key_hash.encode('utf-8'))

    def save_master_key(self):
        data = {'master_key': self.master_key_hash}
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def master_key_exists(self):
        return self.master_key_hash is not None
