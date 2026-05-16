import os 
import subprocess

import sys
from pathlib import Path

project_name = ""

def CreatFolder():
    global project_name
    arg = input("do you wnat to creat a folder Y|N :").lower().strip()
    if arg != "y":
        print("Good byy...")
        return False
    
    project_name = input("Give you folder a name:")

    if not project_name.strip():
        print("Folder name cannot be empty")
        return False

    try:
        os.makedirs(project_name, exist_ok=True)
        print(f'Your folder is created {project_name}')
    except Exception as e:
        print(f"Error: {e}")

    
    return True

def CreatEnviroment():
    arg = input("do you wnat to creat Python enviroment Y|N :").lower().strip()
    if arg != "y":
        print("Good byy...")
        return False
    try:
        subprocess.run(["python", "--version"], check=True)
        if sys.version_info >= (3, 8):
            print("Python is installed")
        
        else:
            print("python version is too old")
            return False
            
  

        
        
        os.chdir(project_name)

        print("creating vertiual enviroment...")

        subprocess.run(["python","-m","venv","venv"],check= True)

        print("virtual enviroment is created successfully")

        print("Now creating some important files and folders")
        Path("README.md").touch()
        Path(".gitignore").touch()
        Path("requirements.txt").touch()
        Path("main.py").touch()
        Path(".env").touch()
        print("Starter files created")

        print("Adding some file inside .gitignore")
        with open(".gitignore", "w") as file:
            file.write("venv/\n")
            file.write("__pycache__/\n")
            file.write(".env\n")
        print("done")



    except Exception as e:
        print(f"Error: {e}")
        return False
    
def git_init():
    arg = input("Do you want to install git Y|N:").lower().strip()

    if arg != "y":
        print("Good byy...")
        return False
    
    try:
        subprocess.run(["git","init"],check=True)
        print("Git initialized successfully")

    except Exception as e:
      print(f"Error: {e}")

def InstallProject():

    arg = input(
        "Do you want to install any packages Y/N: "
    ).lower().strip()

    if arg != "y":
        print("Skipping package installation...")
        return False

    arg2 = input(
        "Enter package names separated by commas: "
    )

    packages = arg2.split(",")

    try:

        for package in packages:

            subprocess.run(
                [
                    "python",
                    "-m",
                    "pip",
                    "install",
                    package.strip()
                ],
                check=True
            )

        print("Packages installed successfully")

        # Create requirements.txt
        with open("requirements.txt", "w") as file:

            subprocess.run(
                ["python", "-m", "pip", "freeze"],
                stdout=file
            )

        print("requirements.txt created successfully")

    except Exception as e:
        print(f"Error: {e}")




folder_created = CreatFolder()

if folder_created:
    CreatEnviroment()
    git_init()
    InstallProject()


  





    









 





    



