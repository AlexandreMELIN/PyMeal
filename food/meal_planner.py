from typing import List

from food.food import Food
from food.meal_preference import MealPreference
import random

class MealItem:
    def __init__(self, food: Food, quantity: float):
        self.food = food
        self.quantity = quantity


class Meal:
    def __init__(self, items: List[MealItem]):
        self.items = items

class TargetMacro:
    def __init__(self, protein: int, carbohydrates: int, fat: int, fiber: int):
        if protein < 0:
            raise ValueError("Protein cannot be negative")
        if carbohydrates < 0:
            raise ValueError("Carbohydrates cannot be negative")
        if fat < 0:
            raise ValueError("Fatness cannot be negative")
        if fiber < 0:
            raise ValueError("Fibers cannot be negative")
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fiber = fiber
        self.fat = fat


def plan_a_breakfast(preference: MealPreference, target_macro: TargetMacro) -> Meal:
    meal = Meal([])
    target_protein = target_macro.protein
    target_carbohydrates = target_macro.carbohydrates
    starch: Food = random.choice(list(preference.starches))
    quantity = _compute_quantity_to_match_macro(starch.nutritional_panel.carbohydrates, target_carbohydrates)
    target_protein -= _compute_macro(starch.nutritional_panel.protein, quantity)
    target_carbohydrates -= _compute_macro(starch.nutritional_panel.carbohydrates, quantity)
    meal.items.append(MealItem(starch, quantity))
    if preference.proteins:
        protein: Food = random.choice(list(preference.proteins))
        if preference.dairies:
            dairy: Food = random.choice(list(preference.dairies))
            quantity = _compute_quantity_to_match_macro(dairy.nutritional_panel.protein, target_protein * 0.3)
            meal.items.append(MealItem(dairy, quantity))
            quantity = _compute_quantity_to_match_macro(protein.nutritional_panel.protein, target_protein * 0.7)
            meal.items.append(MealItem(protein, quantity))
        else:
            quantity = _compute_quantity_to_match_macro(protein.nutritional_panel.protein, target_protein)
            meal.items.append(MealItem(protein, quantity))
    elif preference.dairies:
        dairy: Food = random.choice(list(preference.dairies))
        meal.items.append(MealItem(dairy, _compute_quantity_to_match_macro(dairy.nutritional_panel.protein, target_protein)))

    return meal

def plan_a_meal(meal_preference: MealPreference, target_macro: TargetMacro) -> Meal:
    meal = Meal([])
    target_protein = target_macro.protein
    target_carbohydrates = target_macro.carbohydrates
    should_include_plants = meal_preference.plants and bool(random.getrandbits(1))
    if should_include_plants:
        plant: Food = random.choice(list(meal_preference.plants))
        quantity = _compute_quantity_to_match_macro(plant.nutritional_panel.carbohydrates, target_carbohydrates / 2)
        target_protein -= _compute_macro(quantity, plant.nutritional_panel.protein)
        target_carbohydrates -= _compute_macro(quantity, plant.nutritional_panel.carbohydrates)
        meal.items.append(MealItem(plant, quantity))

    starch: Food = random.choice(list(meal_preference.starches))
    quantity = _compute_quantity_to_match_macro(starch.nutritional_panel.carbohydrates, target_carbohydrates)
    if should_include_plants:
        quantity = _compute_quantity_to_match_macro(starch.nutritional_panel.carbohydrates, target_carbohydrates / 2)
    target_protein -= _compute_macro(quantity, starch.nutritional_panel.protein)
    target_carbohydrates -= _compute_macro(quantity, starch.nutritional_panel.carbohydrates)
    meal.items.append(MealItem(starch, quantity))

    protein: Food = random.choice(list(meal_preference.proteins))
    quantity = _compute_quantity_to_match_macro(protein.nutritional_panel.carbohydrates, target_protein)
    meal.items.append(MealItem(protein, quantity))

    vegetable: Food = random.choice(list(meal_preference.vegetables))
    quantity = 80 * random.randint(1,4)
    meal.items.append(MealItem(vegetable, quantity))

    if meal_preference.fruits and bool(random.getrandbits(1)):
        fruit = random.choice(list(meal_preference.fruits))
        meal.items.append(MealItem(fruit, 80))
    return meal

def _compute_quantity_to_match_macro(macro_for_100_grams: float, target: float) -> float:
    return target / macro_for_100_grams * 100

def _compute_macro(quantity: float, reference: float) -> float:
    return (quantity / 100) * reference