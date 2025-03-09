# lib/helpers.py
from models.meal import Meal
from models.ingredient import Ingredient 

def display_meals():
    meals = Meal.get_all()
    if not meals:
        print("No meals found.")


def exit_program():
    print("Goodbye!")
    exit()
