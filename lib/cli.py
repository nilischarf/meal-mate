# lib/cli.py

from helpers import (
    list_categories,
    add_category,
    delete_category,
    add_meal,
    delete_meal,
    edit_meal
)


def main():
    while True: # not exit 
        menu()
        choice = input("> ").strip()
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_categories()
        elif choice == "2": # delete category 
            add_category()
        elif choice == "3":
            delete_category()
        elif choice == "4":
            add_meal()
        elif choice == "5":
            delete_meal()
        elif choice == "6":
            edit_meal()
        else:
            print("Invalid choice")


def menu():
    print("MealMate Menu:")
    print("Please select an option:")
    print("0. Exit Program")
    print("1. View Categories")
    print("2. Add Category") 
    print("3. Delete Category") 
    print("4. Add Meal to Category") 
    print("5. Delete Meal")
    print("6. Edit Meal")


if __name__ == "__main__":
    main()
