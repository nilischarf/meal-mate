# lib/helpers.py

from models.category import Category
from models.meal import Meal

def list_categories():
    categories = Category.get_all()
    if not categories:
        print("No categories found. Please add a category.")
        return None
    else:
        print("Categories:")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category.name}") 
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
    category_index = int(input("Enter category number to delete: ")) - 1
    if 0 <= category_index < len(categories):
        categories[category_index].delete()
        print("Category deleted successfully.")
    else:
        print("Invalid category number.")

def list_meals(category):
    meals = category.meals()
    if not meals:
        print("No meals found in this category.")
    else:
        for index, meal in enumerate(meals, start=1):
            print(f"{index}. {meal}")
    return meals

def create_meal(category):
    name = input("Enter meal name: ")
    easiness = int(input("Enter easiness (1-5): "))
    prep_time = int(input("Enter prep time (in minutes): "))
    rating = int(input("Enter rating (1-5): "))
    meal = Meal.create(name, easiness, prep_time, rating, category.id)
    print(f"Created Meal: {meal}")

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

def edit_meal(category):
    meals = list_meals(category)
    if not meals:
        return
    meal_index = int(input("Enter meal number to edit: ")) - 1
    if 0 <= meals_index < len(meals):
        meal = meals[meals_index]
        meal.name = input(f"Enter new name ({meal.name}): " or meal.name)
        meal.easiness = int(input(f"Enter new easiness (1-5), current {meal.easiness}): ") or meal.easiness)
        meal.prep_time = int(input(f"Enter new prep time (current {meal.prep_time}): " or meal.prep_time))
        meal.rating = int(input(f"Enter new rating (1-5), (current {meal.rating}): " or meal.rating))
        meal.update()
        print("Meal edited successfully.")
    else:
        print("Invalid meal number.")

def exit_program():
    print("Goodbye!")
    exit()
