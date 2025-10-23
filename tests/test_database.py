import allure

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import TestBunList, TestIngredientList


class TestDatabase:
    @allure.title("Тест добавления булочки в базу данных")
    def test_add_bun(self, data_base):
        data_base.buns.append(Bun(TestBunList.BUNS[0]['name'], TestBunList.BUNS[0]['price']))
        assert len(data_base.buns) == 4
        assert data_base.buns[3].name == TestBunList.BUNS[0]['name']

    @allure.title("Тест удаления булочки из базы данных")
    def test_remove_bun(self, data_base):
        data_base.buns.remove(data_base.buns[0])
        assert len(data_base.buns) == 2
        assert data_base.buns[0].name == "white bun"

    @allure.title("Тест получения доступных булочек")
    def test_available_buns(self, data_base):
        assert len(data_base.available_buns()) == 3

    @allure.title("Тест на добавление соуса в список ингредиентов")
    def test_available_ingredients_sauce(self, data_base):
        data_base.ingredients.append(Ingredient(TestIngredientList.INGREDIENTS[3]['type'],
                                                TestIngredientList.INGREDIENTS[3]['name'],
                                                TestIngredientList.INGREDIENTS[3]['price']))
        assert len(data_base.available_ingredients()) == 7
        assert data_base.ingredients[6].name == TestIngredientList.INGREDIENTS[3]['name']

    @allure.title("Тест на удаление соуса из списка ингредиентов")
    def test_remove_ingredient_sauce(self, data_base):
        data_base.ingredients.remove(data_base.ingredients[0])
        assert len(data_base.ingredients) == 5
        assert data_base.ingredients[0].name == "sour cream"

    @allure.title("Тест на добавление начинки в список ингредиентов")
    def test_available_ingredients_filling(self, data_base):
        data_base.ingredients.append(Ingredient(TestIngredientList.INGREDIENTS[4]['type'],
                                                TestIngredientList.INGREDIENTS[4]['name'],
                                                TestIngredientList.INGREDIENTS[4]['price']))
        assert len(data_base.available_ingredients()) == 7
        assert data_base.ingredients[6].name == TestIngredientList.INGREDIENTS[4]['name']

    @allure.title("Тест на удаление начинки из списка ингредиентов")
    def test_remove_ingredient_filling(self, data_base):
        data_base.ingredients.remove(data_base.ingredients[3])
        assert len(data_base.ingredients) == 5
        assert data_base.ingredients[3].name == "dinosaur"

    @allure.title("Тест на получение доступных ингредиентов")
    def test_available_ingredients(self, data_base):
        assert len(data_base.available_ingredients()) == 6