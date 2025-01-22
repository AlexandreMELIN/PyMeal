from abc import abstractmethod
from typing import List

from food.food import Food

class MealItem:
    def __init__(self, food: Food, quantity: float):
        self.food = food
        self.quantity = quantity


class Meal:
    def __init__(self, items: List[MealItem]):
        self.items = items

    def __str__(self):
        return "\t".join([f"{i.food.food_name}: {i.quantity}g\n" for i in self.items])

class MealOrganization:
    @abstractmethod
    def get_meals(self) -> List[Meal]:
        pass

class MealsForADay(MealOrganization):
    def __init__(self, breakfast: Meal, lunch: Meal, dinner: Meal):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

    def get_meals(self) -> List[Meal]:
        return [self.breakfast, self.lunch, self.dinner]

    def __str__(self):
        return "\n\t".join(map(str, self.get_meals()))

class MealsForAWeek(MealOrganization):
    def __init__(self, monday: MealsForADay, tuesday: MealsForADay, wednesday: MealsForADay, thursday: MealsForADay, friday: MealsForADay, saturday: MealsForADay, sunday: MealsForADay):
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday

    def get_meals(self) -> List[Meal]:
        all_days = [self.monday, self.tuesday, self.wednesday, self.thursday,self.friday, self.saturday, self.sunday]
        all_meals = map(lambda day: day.get_meals(), all_days)
        return sum(all_meals, [])

    def __str__(self):
        return f"""
Monday : \n{str(self.monday)}
Tuesday : \n{str(self.tuesday)}
Wednesday : \n{str(self.wednesday)}
Thursday : \n{str(self.thursday)}
Friday : \n{str(self.friday)}
Saturday : \n{str(self.saturday)}
Sunday : \n{str(self.sunday)}
"""

