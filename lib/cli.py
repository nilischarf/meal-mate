# lib/cli.py

from helpers import (
    display_meals,
    add_meal,
    delete_meal,
    add_ingredient,
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
        elif choice == "3":
            delete_meal()
        elif choice == "4":
            add_ingredient()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit program")
    print("1. View all meals")
    print("2. Add a meal") 
    print("3. Delete a meal") 
    print("4. Add an ingredient") 


if __name__ == "__main__":
    main()
