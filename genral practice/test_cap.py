import unittest
import cap
class TestCap(unittest.TestCase):
    def test_one(self):
        text = 'hello'
        result = cap.my_text(text)
        self.assertEqual(result,'Hello')

    def test_two(self):
        text = "ahumuza asiimwe"
        result = cap.my_text(text)
        self.assertEqual(result,'Ahumuza Asiimwe')


if __name__ == "__main__":
        unittest.main()

