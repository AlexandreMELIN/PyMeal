class NutritionalPanel:
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
        self.calories = 9 * self.fat + 4 * self.carbohydrates + 4 * self.protein + 2 * self.fiber

    def __str__(self):
        return f"protein: {self.protein}g, carbs: {self.carbohydrates}g, fat: {self.fat}g, fiber: {self.fiber}g, calories: {self.calories} Kcal"


def add_two_nutritional_panel(nutritional_panel1: NutritionalPanel, nutritional_panel2: NutritionalPanel) -> NutritionalPanel:
    return NutritionalPanel(nutritional_panel1.protein + nutritional_panel2.protein,
                            nutritional_panel1.carbohydrates + nutritional_panel2.carbohydrates,
                            nutritional_panel1.fat + nutritional_panel2.fat,
                            nutritional_panel1.fiber + nutritional_panel2.fiber
                            )