# lib/cli.py

from helpers import (
    list_categories,
    add_category,
    delete_category,
    add_meal,
    delete_meal,
    edit_meal
)


def categories():
    choice = ""
    while choice != 0: 
        menu()
        choice = input("> ").strip()
        if choice == "?": # is an int taht represents one of the categories --> how do i make my categories into ints if they get to choose category names 
            category = categories[int(choice) - 1]
            meals_loop(category)
            categories = list_categories()
        elif choice == "A": 
            add_category()
        elif choice == "D":
            delete_category()
        
        elif choice == ???: 
            # grab the category that i picked 
            category = categories[int(choice) - 1]
            meals_loop(category)
        else:
            print("Invalid choice")
    exit_program()

# meals loop (category)
def meals_loop(category):
    category.meals() # category model has to have an instance method meals that returns meals in category
    # elif choice == "4":
        #     add_meal()
        # elif choice == "5":
        #     delete_meal()
        # elif choice == "6":
        #     edit_meal()

# meal loop (meal)

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


# def __str__(self): # move to cli 
#         return f"{self.name} ({self.category})"

# def __str__(self): # move to cli 
#         return f"{self.name}"