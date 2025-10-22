import os
import core.auth as auth
import core.commands as commands

os.system("cls")
print("===================================")
print("        🛡️  WARDEN CLI v1.0")
print("===================================")

if auth.verify_root_password():
    print("Welcome to Warden CLI!")

    commands.command_loop()