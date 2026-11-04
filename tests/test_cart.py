import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm 20 đĩa DVD đầu tiên -> phải thành công (True)
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=10.0)))
        
        # Đĩa thứ 21 vượt quá giới hạn -> bắt buộc phải trả về False
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", cost=10.0)))

    def test_remove_dvd(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test DVD", cost=15.0)
        cart.add_dvd(dvd)
        self.assertTrue(cart.remove_dvd(dvd))
        self.assertFalse(cart.remove_dvd(dvd))
    def test_discount_calculation(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", cost=100.0))
        # Giảm 20% của 100$ thì tổng tiền phải còn 80$
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_invalid_percent(self):
        cart = Cart()
        # Phần trăm giảm giá ngoài khoảng [0, 100] phải ném ra ValueError
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(-10)


if __name__ == "__main__":
    unittest.main()