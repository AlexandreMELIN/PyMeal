from food.food import Food


class MealPreference:
    def __init__(self, proteins: set[Food], plants: set[Food], vegetables: set[Food], starches: set[Food], dairies: set[Food], fruits: set[Food]):
        self.proteins = proteins
        self.plants = plants
        self.vegetables = vegetables
        self.starches = starches
        self.dairies = dairies
        self.fruits = fruits