import unittest
import change_text


class TestChangeText(unittest.TestCase):
    def text_upper(self):
        word = "good morning"
        result = change_text.convert_upper(word)

        self.assertEqual(result, "GOOD MORNING")


if __name__ == '__main__':
    unittest.main()
