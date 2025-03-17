# lib/cli.py

from helpers import (
    list_categories,
    create_category,
    delete_category,
    list_meals,
    create_meal,
    delete_meal,
    edit_meal,
    exit_program
)


def categories():
    choice = ""
    while choice != "E": 
        menu()
        choice = input("> ").strip()
        categories = list_categories()

        if isinstance(choice, int) and 1 <= int(choice) <= len(categories):
            category = categories[int(choice) - 1]
            meals(category)
        elif choice.upper() == "C":
            create_category()
        elif choice.upper() == "D":
            delete_category()
        else:
            print("Invalid choice")
    exit_program()

def meals(category):
    choice = ""
    while choice != "B": 
        print(f"{category.name} Meals Menu:")
        options = ["List meals", "Add meal", "Delete meal", "Edit meal", "Go back"]
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        
        choice = input("Enter your choice: ")
        if choice == "L":
            list_meals(category)
        elif choice == "C":
            create_meal(category)
        elif choice == "D":
            delete_meal(category)
        elif choice == "E":
            edit_meal(category)
        else:
            print("Invalid choice. Please try again.")
    # go back a level
       


def menu():
    print("MealMate Menu:")
    options = ["List categories", "Create category", "Delete category", "Select category", "Exit"]
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

if __name__ == "__main__":
    main()