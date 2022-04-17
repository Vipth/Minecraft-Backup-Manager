import os, shutil
from time import sleep

# Constants
PROGRAM_TITLE = "Backup Manager"
USERNAME = os.getlogin()
MINECRAFT_FOLDER = f'C:/Users/{USERNAME}/AppData/Roaming/.minecraft'
SAVES_FOLDER = f'{MINECRAFT_FOLDER}/saves'
BACKUP_FOLDER = f'C:/Users/{USERNAME}/AppData/Roaming/.minecraft/Backup Manager'
EXIT = False

# QOL
os.system('echo off')
os.system('color 0a')
os.system(f'title {PROGRAM_TITLE}')

# Checks to see if the backup folder exists. If not, it prompts to create it.
def checkBackupFolder() -> None:
    if not os.path.exists(BACKUP_FOLDER):
        os.system('cls')
        print("Backup folder not found.")
        print("Would you like to create a backup folder?")
        print("1. Yes")
        print("2. No")
        while True:
            choice = input("Choice: ")
            if choice == "1":
                os.mkdir(BACKUP_FOLDER)
                print(f"Backup folder created as '{BACKUP_FOLDER}'.")
                os.system('cls')
                break
            elif choice == "2":
                print("Exiting...")
                global EXIT
                EXIT = True
                return
            else:
                print("Invalid choice.")

# Deletes the backup folder if it exists (And everything in it, obviously).
def deleteBackupFolder() -> None:
    os.system('cls')
    print("Are you sure you want to delete the backup folder?")
    print("1. Yes")
    print("2. No")
    while True:
        choice = input("Choice: ")
        if choice == "1":
            print("Deleting backup folder...")
            shutil.rmtree(BACKUP_FOLDER)
            print("Backup folder deleted.")
            break
        elif choice == "2":
            break
        else:
            print("Invalid choice.")

# Gets the saves in the saves folder.
def getSaves() -> list:
    saves = []
    for file in os.listdir(SAVES_FOLDER):
        saves.append(file)
    return saves

# Gets the backups in the backup folder.
def getBackups() -> list:
    backups = []
    for file in os.listdir(BACKUP_FOLDER):
        backups.append(file)
    return backups

# Creates a backup of any or all worlds chosen by the user.
def backupWorld() -> None:
    os.system('cls')
    print("Which world would you like to backup?")
    saves = getSaves()
    if len(saves) == 0:
        print("No saves found.")
        sleep(1)
        return
    for i, v in enumerate(saves):
        print(f"{i + 1}. {v}")
    print(f'{len(saves) + 1}. All.')
    print(f'{len(saves) + 2}. Cancel.')
    while True:
        choice = input("Choice: ")
        if choice.isdigit() and int(choice) <= len(saves):
            choice = int(choice) - 1
            choice = saves[choice]
            os.system('cls')
            print(f"Backing up '{choice}'...")
            if os.path.exists(f'{BACKUP_FOLDER}/{choice}'):
                shutil.rmtree(f'{BACKUP_FOLDER}/{choice}')
            worldPath = f'{SAVES_FOLDER}/{choice}'
            shutil.copytree(src=worldPath, dst=f'{BACKUP_FOLDER}/{choice}', copy_function = shutil.copy2)
            break
        if choice.isdigit() and int(choice) == len(saves) + 1:
            os.system('cls')
            for save in getSaves():
                print(f"Backing up '{save}'...")
                if os.path.exists(f'{BACKUP_FOLDER}/{save}'):
                    shutil.rmtree(f'{BACKUP_FOLDER}/{save}')
                shutil.copytree(src=f'{SAVES_FOLDER}/{save}', dst=f'{BACKUP_FOLDER}/{save}', copy_function = shutil.copy2)
            break
        elif choice.isdigit() and int(choice) == len(saves) + 2:
            os.system('cls')
            return print("Cancelled.")
        else:
            print("Invalid choice.")
    print("Backup complete.")

# Deletes a backup of any or all worlds chosen by the user.
def deleteBackup() -> None:
    os.system('cls')
    print("Which world would you like to delete?")
    backups = getBackups()
    if len(backups) == 0:
        print("No backups found.")
        sleep(1)
        return
    for i, v in enumerate(backups):
        print(f"{i + 1}. {v}")
    print(f'{len(backups) + 1}. All.')
    print(f'{len(backups) + 2}. Cancel.')
    while True:
        choice = input("Choice: ")
        if choice.isdigit() and int(choice) <= len(backups):
            choice = int(choice) - 1
            choice = backups[choice]
            os.system('cls')
            print(f"Deleting '{choice}'...")
            break
        elif choice.isdigit() and int(choice) == len(backups) + 1:
            os.system('cls')
            for backup in getBackups():
                print(f"Deleting '{backup}'...")
                shutil.rmtree(f'{BACKUP_FOLDER}/{backup}')
            break
        elif choice.isdigit() and int(choice) == len(backups) + 2:
            os.system('cls')
            return print("Cancelled.")
        else:
            print("Invalid choice.")
    if os.path.exists(f'{BACKUP_FOLDER}/{choice}'):
        shutil.rmtree(f'{BACKUP_FOLDER}/{choice}')
    print("Backups deleted.")

# Restores a backup of any or all worlds chosen by the user.
def restoreBackup() -> None:
    os.system('cls')
    print("Which world would you like to restore?")
    backups = getBackups()
    if len(backups) == 0:
        print("No backups found.")
        sleep(1)
        return
    for i, v in enumerate(backups):
        print(f"{i + 1}. {v}")
    print(f'{len(backups) + 1}. All.')
    print(f'{len(backups) + 2}. Cancel.')
    while True:
        choice = input("Choice: ")
        if choice.isdigit() and int(choice) <= len(backups):
            choice = int(choice) - 1
            choice = backups[choice]
            os.system('cls')
            print(f"Restoring '{choice}'...")
            worldPath = f'{SAVES_FOLDER}/{choice}'
            if os.path.exists(worldPath):
                shutil.rmtree(worldPath)
            shutil.copytree(src=f'{BACKUP_FOLDER}/{choice}', dst=worldPath, copy_function = shutil.copy2)
            break
        elif choice.isdigit() and int(choice) == len(backups) + 1:
            os.system('cls')
            for save in getSaves():
                print(f"Restoring '{save}'...")
                worldPath = f'{SAVES_FOLDER}/{save}'
                if os.path.exists(worldPath):
                    shutil.rmtree(worldPath)
                shutil.copytree(src=f'{BACKUP_FOLDER}/{save}', dst=worldPath, copy_function = shutil.copy2)
            break
        elif choice.isdigit() and int(choice) == len(backups) + 2:
            os.system('cls')
            return print("Cancelled.")
        else:
            print("Invalid choice.")
    print("Restore complete.")

def main() -> None:
    os.system('cls')
    global EXIT
    while EXIT == False:
        checkBackupFolder()
        if EXIT == True: return
        print("What would you like to do?")
        print("1. Backup a world.")
        print("2. Restore a backup.")
        print("3. Delete a backup.")
        print(f"4. Delete {PROGRAM_TITLE} Folder.")
        print("5. Exit.")
        choice = input("Choice: ")
        if choice == "1":
            backupWorld()
        elif choice == "2":
            restoreBackup()
        elif choice == "3":
            deleteBackup()
        elif choice == "4":
            deleteBackupFolder()
        elif choice == "5":
            EXIT = True
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()