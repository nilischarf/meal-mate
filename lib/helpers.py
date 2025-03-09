# lib/helpers.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.meal import Meal
from models.ingredient import Ingredient

def display_meals():
    meals = Meal.get_all()
    if not meals:
        print("No meals found.")
    else:
        for meal in meals:
            print(f"- {meal}")


def exit_program():
    print("Goodbye!")
    exit()
