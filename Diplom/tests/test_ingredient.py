import allure

import data
from praktikum.ingredient import Ingredient


class TestIngredient:

    @allure.title("Тест получения цены ингредиента")
    def test_get_price(self):
        ingredient = Ingredient(data.BurgerName.INGREDIENT_TYPE_ONE,
                                data.BurgerName.INGREDIENT_NAME_ONE,
                                data.BurgerName.INGREDIENT_PRICE_ONE)
        assert ingredient.get_price() == data.BurgerName.INGREDIENT_PRICE_ONE

    @allure.title("Тест получения названия ингредиента")
    def test_get_name(self):
        ingredient = Ingredient(data.BurgerName.INGREDIENT_TYPE_ONE,
                                data.BurgerName.INGREDIENT_NAME_ONE,
                                data.BurgerName.INGREDIENT_PRICE_ONE)
        assert ingredient.get_name() == data.BurgerName.INGREDIENT_NAME_ONE

    @allure.title("Тест получения типа ингредиента")
    def test_get_type(self):
        ingredient = Ingredient(data.BurgerName.INGREDIENT_TYPE_ONE,
                                data.BurgerName.INGREDIENT_NAME_ONE,
                                data.BurgerName.INGREDIENT_PRICE_ONE)
        assert ingredient.get_type() == data.BurgerName.INGREDIENT_TYPE_ONE