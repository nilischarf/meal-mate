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
    # categories loop 
    choice = ""
    while choice != 0: # not exit 
        menu()
        choice = input("> ").strip()
        #if choice == "0":
            
        if choice == "1": # change numbers to letters 
            categories = list_categories()
        elif choice == "2": 
            add_category()
        elif choice == "3":
            delete_category()
        # elif choice == "4":
        #     add_meal()
        # elif choice == "5":
        #     delete_meal()
        # elif choice == "6":
        #     edit_meal()
        elif choice == ???: # is an int taht represents one of the categories 
            # grab the category that i picked 

        else:
            print("Invalid choice")
    exit_program()

# meals loop (category)


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
