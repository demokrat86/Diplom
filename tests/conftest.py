import pytest

from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING as FILLING


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def data_base():
    database = Database()
    return database


@pytest.fixture
def mock_set_buns():        # мок для булочки (название и цена)
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Булочка с приветом"
    mock_bun.get_price.return_value = 100
    return mock_bun


@pytest.fixture
def mock_add_ingredients_filling():     # мок для ингредиентов - начинка (тип ингредиента, название и цена)
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = FILLING
    mock_ingredient.get_name.return_value = 'Адская Креветка'
    mock_ingredient.get_price.return_value = 666
    return mock_ingredient


@pytest.fixture
def mock_add_ingredients_sauce():       # мок для ингредиентов - соус (тип ингредиента, название и цена)
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = SAUCE
    mock_ingredient.get_name.return_value = 'Соевый соус, простой соевый соус'
    mock_ingredient.get_price.return_value = 999
    return mock_ingredient