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

def print_separator():
    print("\n" + "*" * 20 + "\n")

def categories():
    choice = ""
    while choice != "4": 
        print_separator()
        menu()
        print_separator()
        choice = input("> ").strip()
        print_separator()

        if choice == "1":
            categories_list = list_categories()
            print_separator()
            if categories_list:
                print("Select a category by letter to enter it, or press Enter to continue: ")
                print_separator()
                while True:  # Loop until a valid category is chosen
                    try:
                        category_choice = input("> ").strip().upper()
                        if category_choice == "":  # User presses Enter to continue
                            break
                        if not category_choice.isalpha() or category_choice not in [chr(65 + i) for i in range(len(categories_list))]:
                            raise ValueError("Invalid category selection. Please enter a valid letter from the list.")
                        category_index = ord(category_choice) - 65
                        category = categories_list[category_index]
                        meals(category)
                        break  # Exit the loop after a valid category is selected
                    except ValueError as e:
                        print(e)
                        print_separator()
            else:
                print("No categories available.")
                print_separator()
        elif choice == "2":
            create_category()
        elif choice == "3":
            delete_category()
        elif int(choice) == 0 or int(choice) > 4:
            print("Invalid choice. Please try again.")
            print_separator()
    exit_program()

def meals(category):
    choice = ""
    while choice != "5": 
        print_separator()
        print(f"{category.name} Meals Menu:")
        options = ["List meals", "Add meal", "Delete meal", "Edit meal", "Go back"]
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        
        print_separator()
        choice = input("Enter your choice: ").strip()
        print_separator()
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
    options = ["List categories", "Create category", "Delete category", "Exit"]
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

if __name__ == "__main__":
    categories()
