from food.food import Food, FoodCategory
from food.meal_planner import plan_a_day, TargetMacro, plan_a_week
from food.nutritional_panel import NutritionalPanel
from food.meal_preference import MealPreference
from grocery.grocery_list import compute_grocery_list

# Create Breakfast Foods
eggs = Food(
    "Eggs",
    FoodCategory.PROTEIN,
    NutritionalPanel(protein=13, carbohydrates=1, fat=11, fiber=0)  # per 100g
)

oats = Food(
    "Oats",
    FoodCategory.STARCH,
    NutritionalPanel(protein=13, carbohydrates=68, fat=7, fiber=10)  # per 100g
)

bread = Food(
    "Whole Wheat Bread",
    FoodCategory.STARCH,
    NutritionalPanel(protein=9, carbohydrates=49, fat=3, fiber=7)  # per 100g
)

white_yogurt = Food(
    "White Yogurt",
    FoodCategory.DAIRY,
    NutritionalPanel(protein=4, carbohydrates=5, fat=3, fiber=0)  # per 100g
)

# Create Main Meal Proteins
salmon = Food(
    "Salmon",
    FoodCategory.PROTEIN,
    NutritionalPanel(protein=22, carbohydrates=0, fat=13, fiber=0)  # per 100g
)

chicken = Food(
    "Chicken Breast",
    FoodCategory.PROTEIN,
    NutritionalPanel(protein=31, carbohydrates=0, fat=4, fiber=0)  # per 100g
)

tofu = Food(
    "Tofu",
    FoodCategory.PROTEIN,
    NutritionalPanel(protein=8, carbohydrates=2, fat=4, fiber=2)  # per 100g
)

shrimps = Food(
    "Shrimps",
    FoodCategory.PROTEIN,
    NutritionalPanel(protein=24, carbohydrates=0, fat=1, fiber=0)  # per 100g
)

beef = Food(
    "Beef",
    FoodCategory.PROTEIN,
    NutritionalPanel(protein=26, carbohydrates=0, fat=15, fiber=0)  # per 100g
)

# Create Starches
potatoes = Food(
    "Potatoes",
    FoodCategory.STARCH,
    NutritionalPanel(protein=2, carbohydrates=17, fat=0, fiber=2)  # per 100g
)

whole_rice = Food(
    "Whole Rice",
    FoodCategory.STARCH,
    NutritionalPanel(protein=7, carbohydrates=76, fat=3, fiber=4)  # per 100g
)

whole_pasta = Food(
    "Whole Pasta",
    FoodCategory.STARCH,
    NutritionalPanel(protein=13, carbohydrates=75, fat=2, fiber=5)  # per 100g
)

# Create Plants
lentils = Food(
    "Lentils (dry)",
    FoodCategory.PLANT,
    NutritionalPanel(protein=25, carbohydrates=63, fat=1, fiber=31)  # per 100g dry
)

chickpeas = Food(
    "Chickpeas (dry)",
    FoodCategory.PLANT,
    NutritionalPanel(protein=20, carbohydrates=61, fat=6, fiber=17)  # per 100g dry
)

red_bean = Food(
    "Red Bean (dry)",
    FoodCategory.PLANT,
    NutritionalPanel(protein=22, carbohydrates=61, fat=1, fiber=15)  # per 100g dry
)

# Create Vegetables
pepper = Food(
    "Bell Pepper",
    FoodCategory.VEGETABLES,
    NutritionalPanel(protein=1, carbohydrates=6, fat=0, fiber=2)  # per 100g
)

leak = Food(
    "Leak",
    FoodCategory.VEGETABLES,
    NutritionalPanel(protein=2, carbohydrates=14, fat=0, fiber=2)  # per 100g
)

green_bean = Food(
    "Green Bean",
    FoodCategory.VEGETABLES,
    NutritionalPanel(protein=2, carbohydrates=7, fat=0, fiber=3)  # per 100g
)

salad = Food(
    "Salad",
    FoodCategory.VEGETABLES,
    NutritionalPanel(protein=1, carbohydrates=3, fat=0, fiber=1)  # per 100g
)

# Create Fruits
apple = Food(
    "Apple",
    FoodCategory.FRUITS,
    NutritionalPanel(protein=0, carbohydrates=14, fat=0, fiber=2)  # per 100g
)

orange = Food(
    "Orange",
    FoodCategory.FRUITS,
    NutritionalPanel(protein=1, carbohydrates=12, fat=0, fiber=2)  # per 100g
)

banana = Food(
    "Banana",
    FoodCategory.FRUITS,
    NutritionalPanel(protein=1, carbohydrates=23, fat=0, fiber=3)  # per 100g
)

kiwi = Food(
    "Kiwi",
    FoodCategory.FRUITS,
    NutritionalPanel(protein=1, carbohydrates=15, fat=1, fiber=3)  # per 100g
)

# Create Dairy
comte_cheese = Food(
    "Comté Cheese",
    FoodCategory.DAIRY,
    NutritionalPanel(protein=27, carbohydrates=0, fat=32, fiber=0)  # per 100g
)

# Create Breakfast Preferences
breakfast_preference = MealPreference(
    proteins={eggs},
    plants=set(),
    vegetables=set(),
    starches={oats, bread},
    dairies={white_yogurt},
    fruits=set()
)

# Create Main Meal Preferences
main_meal_preference = MealPreference(
    proteins={salmon, chicken, tofu, shrimps, beef},
    plants={lentils, chickpeas, red_bean},
    vegetables={pepper, leak, green_bean, salad},
    starches={potatoes, whole_rice, whole_pasta},
    fruits={apple, orange, banana, kiwi},
    dairies={comte_cheese}
)

# Example usage:
if __name__ == "__main__":
    # Print some example nutritional information
    target_macro = TargetMacro(1.6*80, 4*80)
    meals = plan_a_day(breakfast_preference, main_meal_preference, target_macro)
    print(meals)
    week_planned = plan_a_week(breakfast_preference, main_meal_preference, target_macro)
    print(week_planned)
    grocery_list = compute_grocery_list(week_planned.get_meals())
    print(grocery_list)