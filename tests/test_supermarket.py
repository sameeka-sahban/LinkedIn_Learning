import pytest

from src.supermarket import Checkout


class TestingSupermarket:

    @pytest.fixture()
    def checkout(self):
        co = Checkout()
        co.add_item_price('a', 1)
        co.add_item_price('b', 1)
        return co

    # def test_can_add_item(self,checkout):
    #     checkout.add_item('a')
    #
    # def test_can_add_item_price(self, checkout):
    #     checkout.add_item_price('a', 1)

    def test_can_calculate_total(self, checkout):
        checkout.add_item('a')
        assert checkout.calculate_total() == 1

    def test_can_add_multiple_items(self, checkout):
        checkout.add_item('a')
        checkout.add_item('b')
        assert checkout.calculate_total() == 2

    def test_can_add_discount_rules(self, checkout):
        checkout.add_discount('a', 3, 2)

    def test_can_apply_discount(self, checkout):
        checkout.add_discount('a', 3, 2)
        checkout.add_item('a')
        checkout.add_item('a')
        checkout.add_item('a')
        assert checkout.calculate_total() == 2

    def test_exception_with_bad_item(self, checkout):
        with pytest.raises(Exception):
            checkout.add_item('c')


