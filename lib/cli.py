# lib/cli.py

from helpers import (
    exit_program,
    display_meals
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. No meals found.") # CHANGE!!


if __name__ == "__main__":
    main()
