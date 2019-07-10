from registration_test import register
import unittest


class TestRegister(unittest.TestCase):

    def test_redister_one(self):

        link = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", register(link), "Ошибка регистрации!")

    def test_redister_two(self):

        link = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", register(link), "Ошибка регистрации!")


if __name__ == '__main__':
    unittest.main()
