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
                print("Select a category by letter to enter it, or select Enter to continue: ")
                category_choice = input("> ").strip().upper()
                if category_choice.isalpha() and "A" <= category_choice < chr(65 + len(categories_list)): # max letter number of meals 
                    category_index = ord(category_choice) - 65 # calculate the position of the letter in the alphabet (subtract 65 from ASCII)
                    category = categories_list[category_index] # get the category at that index
                    meals(category)
                else:
                    print()
            else:
                print("No categories available.")
        elif choice == "2":
            create_category()
        elif choice == "3":
            delete_category()
        elif int(choice) == 0 or int(choice) > 4:
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
    options = ["List categories", "Create category", "Delete category", "Exit"]
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

if __name__ == "__main__":
    categories()

# meals loop is good!
# categories - 
# 4) look into ord, chr, +/- 65