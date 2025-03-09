# lib/cli.py

from helpers import (
    display_meals,
    exit_program
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            display_meals()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View all meals") 


if __name__ == "__main__":
    main()
