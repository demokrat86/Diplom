from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING as FILLING


class BurgerName:      #названия бургера используемого в тестах
    BUN_NAME = "Черная Мамба"
    BUN_PRICE = 10000
    INGREDIENT_NAME_ONE = "Кетчуп"
    INGREDIENT_PRICE_ONE = 100
    INGREDIENT_TYPE_ONE = SAUCE
    INGREDIENT_NAME_TWO = "Индейка"
    INGREDIENT_PRICE_TWO = 200
    INGREDIENT_TYPE_TWO = FILLING


class TestBunList:      #названия булочек используемых в тестах
    BUNS = [{'name': 'Black Mamba', 'price': 10000},
            {'name': 'Dirty Redneck', 'price': 10},
            {'name': 'White Power', 'price': 1000},
            {'name': 'USSR', 'price': 100}]


class TestIngredientList:       #названия ингредиентов используемых в тестах
    INGREDIENTS = [{'name': 'Ketchup', 'type': SAUCE, 'price': 100},
                   {'name': 'Mayonnaise', 'type': SAUCE, 'price': 200},
                   {'name': 'Cheese sauce', 'type': SAUCE, 'price': 300},
                   {'name': 'Сметана', 'type': SAUCE, 'price': 100},
                   {'name': 'Vegetables', 'type': FILLING, 'price': 200},
                   {'name': 'Shrimps', 'type': FILLING, 'price': 200},
                   {'name': 'Turkey', 'type': FILLING, 'price': 200},
                   {'name': 'Сосиска', 'type': FILLING, 'price': 200}]