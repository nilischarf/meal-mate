# lib/helpers.py

from models.category import Category
from models.meal import Meal

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
    print(f"Created category: {category}")
    return category

def delete_category():
    categories = list_categories()
    if not categories:
        return
    letter_input = input("Enter category letter to delete: ").upper()
    category_index = ord(letter_input) - 65 
    if 0 <= category_index < len(categories):
        category_to_delete = categories[category_index]
        meals = category_to_delete.meals()
        if meals:
            for meal in meals:
                meal.delete()
        category_to_delete.delete()
        print("Category and its meals deleted successfully.")
    else:
        print("Invalid category number.")

def list_meals(category):
    meals = category.meals()
    if not meals:
        print("No meals found in this category.")
    else:
        for index, meal in enumerate(meals, start=1):
            print(f"{index}. Name: {meal.name}, Easiness: {meal.easiness}, Prep Time: {meal.prep_time}, Rating: {meal.rating}")
    return meals

def create_meal(category):
    name = input("Enter meal name: ")
    easiness = int(input("Enter easiness (1-5): "))
    prep_time = int(input("Enter prep time (in minutes): "))
    rating = int(input("Enter rating (1-5): "))
    meal = Meal.create(name, easiness, prep_time, rating, category.id)
    print(f"Created Meal - Name: {meal.name}, Easiness: {meal.easiness}, Prep Time: {meal.prep_time}, Rating: {meal.rating}")

def delete_meal(category):
    meals = list_meals(category)
    if not meals:
        return
    meal_index = int(input("Enter meal number to delete: ")) - 1
    if 0 <= meal_index < len(meals):
        meals[meal_index].delete()
        print("Meal deleted successfully.")
    else:
        print("Invalid meal number.")

# add try/except 
def edit_meal(category):
    meals = list_meals(category)
    if not meals:
        return
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
        meal.prep_time = int(new_prep_time) if new_prep_time.isdigit() else meal.prep_time
        meal.easiness = get_valid_input(f"Enter new easiness (1-5), current ({meal.easiness}): ", meal.easiness)
        meal.rating = get_valid_input(f"Enter new rating (1-5), (current {meal.rating}): ", meal.rating)
        
        try: 
            meal.update()
            print("Meal edited successfully.")
        except Exception as e:
            print(f"An error occured while updating the meal: {e}") 

    else:
        print("Invalid meal number.")

def exit_program():
    print("Goodbye!")
    exit()


# stars and spaces, readme 