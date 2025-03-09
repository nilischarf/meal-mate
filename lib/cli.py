# lib/cli.py

from helpers import (
    display_meals,
    add_meal,
    exit_program
)


def main():
    while True:
        menu()
        choice = input("> ").strip()
        if choice == "0":
            exit_program()
        elif choice == "1":
            display_meals()
        elif choice == "2":
            add_meal()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit program")
    print("1. View all meals")
    print("2. Add a meal") 


if __name__ == "__main__":
    main()
