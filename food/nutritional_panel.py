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