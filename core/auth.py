import os
import bcrypt

PASSWORD_FILE = "data/root.pass"

def check_or_create_root_password():
  if not os.path.exists("data"):
    os.makedirs("data")

  if not os.path.exists(PASSWORD_FILE):
    print("Let's set up your root password.\n")

    while True:
      root_password = input("Create root password: ")

      if len(root_password) < 4:
        print("Password must be at least 4 characters long. Please try again.\n")
        continue

      confirm_password = input("Confirm root password: ")

      if root_password != confirm_password:
        print("Passwords do not match. Please try again.\n")
      else:
        root_password = root_password.encode('utf-8')
        hashed = bcrypt.hashpw(root_password, bcrypt.gensalt())
        with open(PASSWORD_FILE, "wb") as f:
          f.write(hashed)
        print("\nRoot password set successfully!\n")
        break

def verify_root_password():
  if not os.path.exists(PASSWORD_FILE):
    check_or_create_root_password()

  with open(PASSWORD_FILE, "rb") as f:
    stored_hash = f.read()

  print("Please enter your root password to continue.\n")
  entered_password = input("Root password: ").encode('utf-8')

  if bcrypt.checkpw(entered_password, stored_hash):
    print("\nAccess granted.\n")
    return True
  else:
    print("\nAccess denied.\n")
    return False