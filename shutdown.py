import os

choice = input("shutdown your computer? (y or n)")

if choice == 'y' or 'Y':
    os.system("shutdown /s")
else:
    print("Exiting program")