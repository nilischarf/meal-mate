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
    while choice != "4": 
        menu()
        choice = input("> ").strip()

        if choice == "1":
            categories_list = list_categories()
            if categories_list:
                print("Select a category by number to enter it, or choose another option: ")
            else:
                print("No categories available.")
        elif choice == "2":
            create_category()
        elif choice == "3":
            delete_category()
        elif choice.isdigit():
            choice = int(choice)
            categories_list = list_categories()
            if 1 <= choice <= len(categories_list):
                category = categories_list[choice - 1]
                meals(category)
            else: 
                print("Invalid category.")
        else:
            print("Invalid choice. Please try again.")
    exit_program()
    

def meals(category):
    choice = ""
    while choice != "5": 
        print(f"{category.name} Meals Menu:")
        options = ["List meals", "Add meal", "Delete meal", "Edit meal", "Go back"]
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            list_meals(category)
        elif choice == "2":
            create_meal(category)
        elif choice == "3":
            delete_meal(category)
        elif choice == "4":
            edit_meal(category)
        elif choice == "5":
            print("Returning to categories menu.")
        else:
            print("Invalid choice. Please try again.")
       


def menu():
    print("MealMate Menu:")
    options = ["List categories", "Create category", "Delete category", "Select category", "Exit"]
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

if __name__ == "__main__":
    categories()

# need to fix delete - why by 1 less? 
# need to fix selection process/category and lisitng meals 