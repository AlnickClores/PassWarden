from cryptography.fernet import Fernet
import os

KEY_PATH = "data/vault.key"

def load_key():
  if not os.path.exists(KEY_PATH):
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as key_file:
      key_file.write(key)
  else:
    with open(KEY_PATH, "rb") as key_file:
      key = key_file.read()
  return key

def get_cipher():
  key = load_key()
  return Fernet(key)

def encrypt_data(data: str) -> bytes:
  cipher = get_cipher()
  return cipher.encrypt(data.encode())

def decrypt_data(data: bytes) -> str:
  cipher = get_cipher()
  return cipher.decrypt(data).decode()