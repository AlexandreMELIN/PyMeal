from enum import Enum

from food.nutritional_panel import NutritionalPanel


class FoodCategory(Enum):
    PROTEIN = "Protein"
    PLANT = "Plant"
    VEGETABLES = "Vegetables"
    STARCH = "Starch"
    DAIRY = "Dairy"
    FRUITS = "Fruits"

class Food:
    def __init__(self, food_name: str, category: FoodCategory, nutritional_panel: NutritionalPanel):
        self.food_name = food_name
        self.category = category
        self.nutritional_panel = nutritional_panel


