# lib/helpers.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.meal import Meal
from models.category import Category

def list_categories():
    categories = Category.get_all()
    if not categories:
        print("No categories found. Please add a category.")
        return None

    else:
        print("Categories:")
        for i, cat in enumerate(categories, start=1):
            print(f"{i}. {cat.name}")
        return categories

def add_category():
    name = input("Enter new category name: ").strip()
    if not name:
        print("Category name cannot be empty.")
        return
    Category.create(name)
    print(f"Category '{name}' added.")

def delete_category():
    name = input("Enter category name to delete: ").strip() 
    category = Category.find_by_name(name)

    if category:
        category.delete()
        print(f"{category} has been deleted.")
    else:
        print("Category not found.")

def add_meal():
    name = input("Enter meal name: ").strip()
    easiness = int(input("Enter easiness (1-5): "))
    prep_time = int(input("Enter prep time (in minutes): "))
    rating = int(input("Enter rating (1-5): "))

    Meal.create(name, easiness, prep_time, rating, category_id)
    print(f"Meal '{meal.name}' added to {category.name}.")

def delete_meal():
    name = input("Enter meal name to delete: ").strip() # want to stay in meal 
    meal = Meal.find_by_name(name)

    if meal:
        meal.delete()
        print(f"{name} has been deleted.")
    else:
        print("Meal not found.")

def edit_meal():
    name = input("Enter meal name to edit: ").strip() # want to stay in meal 
    meal = Meal.find_by_name(name)
    if not meal: 
        print("Meal not found.")
        return
    
    new_easiness = input("New easiness (1-5, press Enter to keep current): ")
    new_prep_time = input("New prep time (press Enter to keep current): ")
    new_rating = input("New rating (1-5, press Enter to keep current): ")

    meal.update(
        new_easiness=int(new_easiness) if new_easiness else None,
        new_prep_time=int(new_prep_time) if new_prep_time else None,
        new_rating=int(new_rating) if new_rating else None,
    )

    print(f"Meal '{meal.name}' updated successfully.1")

def exit_program():
    print("Goodbye!")
    exit()
