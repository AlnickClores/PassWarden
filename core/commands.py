import os
import re
from InquirerPy import inquirer

def mkvlt(name): # create vault
    path = f"data/vaults/{name}.txt"

    if os.path.exists(path):
        print(f"Vault '{name}' already exists.")
    else:
        os.makedirs("data/vaults", exist_ok=True)
        with open(path, "w") as f:
            f.write("")
        print(f"Vault '{name}' created successfully.")

def ntrvlt(name): # enter account in vault
    path = os.path.join("data/vaults", f"{name}.txt")
    if not os.path.exists(path):
        print(f"Vault '{name}' not found. Use 'mkvlt' to create it first.")
        return

    print(f"\nAdding new account to vault '{name}'\n")
    account_name = input("Name of the account: ")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")

    entry = (
        f"Account: {account_name}\n"
        f"Username: {username}\n"
        f"Email: {email}\n"
        f"Password: {password}\n"
    )

    # Append with proper separator
    with open(path, "a") as f:
        if os.path.getsize(path) > 0:
            f.write("-----\n")
        f.write(entry.strip() + "\n")

    print(f"✅ Account '{account_name}' added to vault '{name}' successfully.")

def rdvlt(name): # read / show contents of vault
    path = os.path.join("data/vaults", f"{name}.txt")

    if not os.path.exists(path):
        print(f"Vault '{name}' not found.")
        return

    print(f"\nVault: '{name}'\n")
    with open(path, "r") as f:
        content = f.read().strip()

    if not content:
        print("No accounts found.\n")
        return

    print(content)
    print()

def edtvlt(name): # edit account in vault
    path = os.path.join("data/vaults", f"{name}.txt")

    if not os.path.exists(path):
        print(f"Vault '{name}' not found.")
        return

    with open(path, "r") as f:
        content = f.read().strip()

    entries = re.split(r"(?:^-{5,}\s*$)", content, flags=re.MULTILINE)
    entries = [e.strip() for e in entries if e.strip()]

    if not entries:
        print(f"No entries found in vault '{name}'.")
        return

    account_names = []
    for entry in entries:
        acc_match = re.search(r"Account:\s*(.*)", entry)
        account_names.append(acc_match.group(1).strip() if acc_match else "Unknown")

    account_names.append("Cancel")

    selected_account = inquirer.select(
        message="Select an account to edit:",
        choices=account_names,
        pointer=">",
    ).execute()

    if selected_account == "Cancel":
        return

    index = account_names.index(selected_account)
    entry = entries[index]

    def get_field(field):
        match = re.search(rf"{field}:\s*(.*)", entry)
        return match.group(1).strip() if match else ""

    account = get_field("Account")
    username = get_field("Username")
    email = get_field("Email")
    password = get_field("Password")

    print("\nLeave blank if you don't want to edit the field.\n")

    new_account = input(f"Account Name [{account}]: ") or account
    new_username = input(f"Username [{username}]: ") or username
    new_email = input(f"Email [{email}]: ") or email
    new_password = input(f"Password [{password}]: ") or password

    updated_entry = (
        f"Account: {new_account}\n"
        f"Username: {new_username}\n"
        f"Email: {new_email}\n"
        f"Password: {new_password}\n"
    )

    entries[index] = updated_entry.strip()
    new_content = "\n-----\n".join(entries).strip() + "\n"

    with open(path, "w") as f:
        f.write(new_content)

    print(f"\n✅ Account '{new_account}' updated successfully in vault '{name}'.")

def rmacc(name): # remove account in vault
    path = os.path.join("data/vaults", f"{name}.txt")

    if not os.path.exists(path):
        print(f"Vault '{name}' not found.")
        return

    with open(path, "r") as f:
        content = f.read().strip()

    entries = re.split(r"(?:^-{5,}\s*$)", content, flags=re.MULTILINE)
    entries = [e.strip() for e in entries if e.strip()]

    if not entries:
        print(f"No entries found in vault '{name}'.")
        return

    account_names = []
    for entry in entries:
        acc_match = re.search(r"Account:\s*(.*)", entry)
        account_names.append(acc_match.group(1).strip() if acc_match else "Unknown")

    selected_account = inquirer.select(
        message="Select an account to delete:",
        choices=account_names,
        pointer=">",
    ).execute()

    index = account_names.index(selected_account)
    entry = entries[index]

    print("\nSelected entry:\n")
    print(entry)

    confirm = inquirer.confirm(
        message=f"Do you want to delete '{selected_account}'?",
        default=False
    ).execute()

    if confirm:
        entries.pop(index)
        updated_content = "\n-----\n".join(entries).strip() + "\n"
        with open(path, "w") as f:
            f.write(updated_content)
        print(f"✅ Account '{selected_account}' deleted successfully.")
    else:
        print("❌ Action canceled.")

def lsvlt(): # read / show created vaults
    vaults = os.listdir("data/vaults")
    if not vaults:
        print("No vaults found.")
        return
    print("\nSaved Vaults:")
    for vault in vaults:
        print(" -", vault)

def rmvlt(name): # remove vault
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
            print(" mkvlt <name>  - create new vault")
            print(" ntrvlt <name> - create new account in vault")
            print(" rdvlt <name>  - read the contents of the vault")
            print(" edtvlt <name> - edit an account in the vault")
            print(" lsvlt         - list all vaults")
            print(" rmvlt <name>  - delete vault")
            print(" rmacc <name>  - delete account in vault")
            print(" exit          - quit program\n")
        elif cmd[0] == "mkvlt" and len(cmd) == 2:
            mkvlt(cmd[1])
        elif cmd[0] == "ntrvlt" and len(cmd) == 2:
            ntrvlt(cmd[1])
        elif cmd[0] == "rdvlt" and len(cmd) == 2:
            rdvlt(cmd[1])
        elif cmd[0] == "edtvlt" and len(cmd) == 2:
            edtvlt(cmd[1])
        elif cmd[0] == "lsvlt":
            lsvlt()
        elif cmd[0] == "rmvlt" and len(cmd) == 2:
            rmvlt(cmd[1])
        elif cmd[0] == "rmacc" and len(cmd) == 2:
            rmacc(cmd[1])
        elif cmd[0] == "exit":
            print("Exiting Warden CLI. Goodbye!")
            break
        else:
            print(f"Unknown command: {cmd[0]}\nType '-help' for a list of commands.")