import allure

from praktikum.bun import Bun
from data import BurgerName


class TestBun:
    @allure.title("Тест получения названия булочки")
    def test_bun_get_name(self):
        bun_name = Bun(BurgerName.BUN_NAME, BurgerName.BUN_PRICE)
        assert bun_name.get_name() == BurgerName.BUN_NAME

    @allure.title("Тест получения цены булочки")
    def test_bun_get_price(self):
        bun_price = Bun(BurgerName.BUN_NAME, BurgerName.BUN_PRICE)
        assert bun_price.get_price() == BurgerName.BUN_PRICE