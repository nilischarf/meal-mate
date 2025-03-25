# lib/helpers.py

from models.category import Category
from models.meal import Meal

def print_separator():
    print("\n" + "*" * 20 + "\n")

def list_categories():
    categories = Category.get_all()
    if not categories:
        print("No categories found. Please add a category.")
        return []
    else:
        print("Categories:")
        for i, category in enumerate(categories, start=1):
            letter = chr(64 + i)
            print(f"{letter}. {category.name}") 
        return categories

def create_category():
    name = input("Enter category name: ")
    category = Category.create(name)
    print_separator()
    print(f"Created category: {category}")
    print_separator()
    return category

def delete_category():
    categories = list_categories()
    if not categories:
        return
    try:
        letter_input = input("Enter category letter to delete: ").upper()
        if letter_input not in [chr(65 + i) for i in range(len(categories))]:
            raise ValueError("Invalid category letter.")
        category_index = ord(letter_input) - 65 
        category_to_delete = categories[category_index]
        meals = category_to_delete.meals()
        if meals:
            for meal in meals:
                meal.delete()
        category_to_delete.delete()
        print_separator()
        print("Category and its meals deleted successfully.")
        print_separator()
    except ValueError as e:
        print(e)

def list_meals(category):
    meals = category.meals()
    print_separator()
    if not meals:
        print("No meals found in this category.")
    else:
        for index, meal in enumerate(meals, start=1):
            print(f"{index}. Name: {meal.name}, Easiness: {meal.easiness}, Prep Time: {meal.prep_time}, Rating: {meal.rating}")
    print_separator()
    return meals

def create_meal(category):
    name = input("Enter meal name: ")
    try: 
        easiness = int(input("Enter easiness (1-5): "))
        if not 1 <= easiness <= 5:
            raise ValueError
        prep_time = int(input("Enter prep time (in minutes): "))
        rating = int(input("Enter rating (1-5): "))
        if not 1 <= rating <= 5:
            raise ValueError
        meal = Meal.create(name, easiness, prep_time, rating, category.id)
        print_separator()
        print(f"Created Meal - Name: {meal.name}, Easiness: {meal.easiness}, Prep Time: {meal.prep_time}, Rating: {meal.rating}")
        print_separator()
    except ValueError:
        print("Invalid input. Please enter valid numbers for easiness (1-5), prep time, and rating (1-5).")

def delete_meal(category):
    meals = list_meals(category)
    if not meals:
        return
    try:
        meal_index = int(input("Enter meal number to delete: ")) - 1
        if 0 <= meal_index < len(meals):
            meals[meal_index].delete()
            print_separator()
            print("Meal deleted successfully.")
            print_separator()
        else:
            print("Invalid meal number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def edit_meal(category):
    meals = list_meals(category)
    if not meals:
        return
    try:
        meal_index = int(input("Enter meal number to edit: ")) - 1
        if 0 <= meal_index < len(meals):
            meal = meals[meal_index]
            print("Press Enter to keep the current value.")
            new_name = input(f"Enter new name ({meal.name}): ")
            new_prep_time = input(f"Enter new prep time (current {meal.prep_time}): ")

            def get_valid_input(prompt, current_value):
                while True:
                    value = input(prompt)
                    if not value:
                        return current_value
                    try:
                        value = int(value)
                        if 1 <= value <= 5:
                            return value
                        else:
                            print("Please enter a number between 1 and 5.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 5.")

            meal.name = new_name if new_name else meal.name
            meal.prep_time = int(new_prep_time) if new_prep_time.isdigit() else meal.prep_time
            meal.easiness = get_valid_input(f"Enter new easiness (1-5), current ({meal.easiness}): ", meal.easiness)
            meal.rating = get_valid_input(f"Enter new rating (1-5), (current {meal.rating}): ", meal.rating)
            
            try: 
                meal.update()
                print_separator()
                print("Meal edited successfully.")
                print_separator()
            except Exception as e:
                print(f"An error occurred while updating the meal: {e}")
        else:
            print("Invalid meal number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def exit_program():
    print_separator()
    print("Goodbye!")
    print_separator()
    exit()


# stars and spaces, readme 