from food.meal_organization import Meal

def compute_grocery_list(meals: list[Meal]) -> dict[str] :
    grocery_list: dict[str][float] = dict[str]()
    for meal in meals:
        for mealItem in meal.items:
            if mealItem.food.food_name not in grocery_list:
                grocery_list[mealItem.food.food_name] = mealItem.quantity
            else:
                grocery_list[mealItem.food.food_name] += mealItem.quantity

    return grocery_list