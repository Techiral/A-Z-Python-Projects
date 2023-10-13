from Crypto.Cipher import AES
import os

class PasswordManager:
    def __init__(self):
        self.key = os.urandom(16) # generate random key for AES encryption
        self.accounts = {}

    def add_account(self, name, password):
        cipher = AES.new(self.key, AES.MODE_EAX)
        encrypted_password, tag = cipher.encrypt_and_digest(password.encode('utf-8'))
        self.accounts[name] = {
            'password': encrypted_password,
            'nonce': cipher.nonce,
            'tag': tag
        }

    def get_password(self, name):
        if name in self.accounts:
            account = self.accounts[name]
            cipher = AES.new(self.key, AES.MODE_EAX, nonce=account['nonce'])
            password = cipher.decrypt_and_verify(account['password'], account['tag'])
            return password.decode('utf-8')
        else:
            return None
