import os

# open file
# read file

def mkvlt(name):
  path = f"data/vaults/{name}.txt"

  if os.path.exists(path):
    print(f"Vault '{name}' already exists.")
  else:
    with open(path, "w") as f:
      f.write("")
    print(f"Vault '{name}' created successfully.")

def ntrvlt(name):
  path = os.path.join("data/vaults", f"{name}.txt")
  if not os.path.exists(path):
    print(f"Vault '{name}' not found. Use 'mkvlt' to create it first.")

  print(f"\nAdding new account to vault '{name}'\n")
  account_name = input("Name of the account: ")
  username = input("Username: ")
  email = input("Email: ")
  password = input("Password: ")

  with open(path, "a") as f:
    f.write(f"Account: {account_name}\n")
    f.write(f"Username: {username}\n")
    f.write(f"Email: {email}\n")
    f.write(f"Password: {password}\n")
    f.write("-" * 20 + "\n")
    
  print(f"Account '{account_name}' added to vault '{name}' successfully.")


def rdvlt(name):
  path = os.path.join("data/vaults", f"{name}.txt")

  if not os.path.exists(path):
    print(f"Vault '{name}' not found.")
    return

  print(f"\nVault: '{name}'")
  with open(path, "r") as f:
    content = f.read().strip()

  if not content:
    print("No accounts found.")

  print(content)
  print()
        


def lsvlt():
  vaults = os.listdir("data/vaults")

  if not vaults:
    print("No vaults found.")
    return
  
  print("\nSaved Vaults:")
  for vault in vaults:
    print(" -", vault)

def rmvlt(name):
  path = f"data/vaults/{name}.txt"

  if os.path.exists(path):
    os.remove(path)
    print(f"Vault '{name}' removed successfully.")
  else:
    print(f"Vault '{name}' does not exist.")

def command_loop():
  while True:
    cmd = input("\nwarden> ").strip().split()

    if not cmd:
      continue

    if cmd[0] == "-help":
      print("\nCommands:")
      print(" mkvlt <name>  - create new file")
      print(" lsvlt         - list all files")
      print(" rmvlt <name>  - delete file")
      print(" exit          - quit program\n")
    elif cmd[0] == "mkvlt" and len(cmd) == 2:
      mkvlt(cmd[1])
    elif cmd[0] == "ntrvlt" and len(cmd) == 2:
      ntrvlt(cmd[1])
    elif cmd[0] == "rdvlt" and len(cmd) == 2:
      rdvlt(cmd[1])
    elif cmd[0] == "lsvlt":
      lsvlt()
    elif cmd[0] == "rmvlt" and len(cmd) == 2:
      rmvlt(cmd[1])
    elif cmd[0] == "exit":
      print("Exiting Warden CLI. Goodbye!")
      break
    else:
      print(f"Unknown command: {cmd[0]}\n Type '-help' for a list of commands.")
    