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
    while choice.upper() != "E": 
        menu()
        choice = input("> ").strip()

        categories = list_categories()
        # if not categories... 

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                meals(category)
            else: 
                print("Invalid category.")
        elif choice.upper() == "C":
            create_category()
        elif choice.upper() == "D":
            delete_category()
        elif choice.upper() == "E":
            exit_program()
        else:
            print("Invalid choice")
    

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
    categories()