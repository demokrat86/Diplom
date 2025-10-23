import allure
import pytest

from unittest.mock import Mock
from unittest.mock import MagicMock


class TestBurger:
    @allure.title('Тест на получение булочки')
    def test_set_buns(self, burger, mock_set_buns):
        burger.set_buns(mock_set_buns)
        assert burger.bun == mock_set_buns

    @allure.title('Тест на добавление ингредиентов')
    def test_add_ingredients(self, burger, mock_add_ingredients_filling, mock_add_ingredients_sauce):
        burger.add_ingredient(mock_add_ingredients_filling)
        burger.add_ingredient(mock_add_ingredients_sauce)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].get_name() == mock_add_ingredients_filling.get_name()
        assert burger.ingredients[0].get_type() == mock_add_ingredients_filling.get_type()
        assert burger.ingredients[0].get_price() == mock_add_ingredients_filling.get_price()
        assert burger.ingredients[1].get_name() == mock_add_ingredients_sauce.get_name()
        assert burger.ingredients[1].get_type() == mock_add_ingredients_sauce.get_type()
        assert burger.ingredients[1].get_price() == mock_add_ingredients_sauce.get_price()

    @allure.title('Тест на удаление ингредиентов')
    def test_remove_ingredients(self, burger, mock_add_ingredients_filling, mock_add_ingredients_sauce):
        burger.add_ingredient(mock_add_ingredients_filling)
        burger.add_ingredient(mock_add_ingredients_sauce)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == mock_add_ingredients_filling.get_name()

    @allure.title('Тест на перемещение ингредиентов')
    def test_move_ingredients(self, burger, mock_add_ingredients_filling, mock_add_ingredients_sauce):
        burger.add_ingredient(mock_add_ingredients_filling)
        burger.add_ingredient(mock_add_ingredients_sauce)
        burger.move_ingredient(1, 0)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].get_name() == mock_add_ingredients_sauce.get_name()
        assert burger.ingredients[1].get_name() == mock_add_ingredients_filling.get_name()

    @pytest.mark.parametrize('bun_price, filling_price, sauce_price, total_price', [(100, 50, 60, 310),
                                                                                    (0, 250, 300, 550),
                                                                                    (1000, 0, 600, 2600),
                                                                                    (300, 50, 0, 650),
                                                                                    (0, 0, 0, 0)])
    @allure.title('Тест на получение цены гамбургера')
    def test_get_price(self, burger, bun_price, filling_price, sauce_price, total_price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_filling = Mock()
        mock_filling.get_price.return_value = filling_price
        mock_sauce = Mock()
        mock_sauce.get_price.return_value = sauce_price
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        assert burger.get_price() == total_price

    @allure.title('Тест на получение рецепта гамбургера')
    def test_get_receipt(self, burger, mock_set_buns, mock_add_ingredients_filling, mock_add_ingredients_sauce):
        mock_set_buns = MagicMock()
        mock_set_buns.get_name.return_value = "Булочка с приветом"

        mock_add_ingredients_filling = MagicMock()
        mock_add_ingredients_filling.get_type.return_value = "filling"
        mock_add_ingredients_filling.get_name.return_value = "Адская Креветка"

        mock_add_ingredients_sauce = MagicMock()
        mock_add_ingredients_sauce.get_type.return_value = "sauce"
        mock_add_ingredients_sauce.get_name.return_value = "Соевый соус, простой соевый соус"

        burger.set_buns(mock_set_buns)
        burger.add_ingredient(mock_add_ingredients_filling)
        burger.add_ingredient(mock_add_ingredients_sauce)

        expected_receipt = (
            "(==== Булочка с приветом ====)\n"
            "= filling Адская Креветка =\n"
            "= sauce Соевый соус, простой соевый соус =\n"
            "(==== Булочка с приветом ====)\n\n"

        )

        receipt = burger.get_receipt()
        assert receipt.strip().startswith(expected_receipt.strip())