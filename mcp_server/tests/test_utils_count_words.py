import unittest

from mcp_server.utils import count_words


class TestCountWords(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_words("This is a test."), 4)

    def test_multiple_spaces(self):
        self.assertEqual(count_words("  Two   spaces "), 2)

    def test_empty(self):
        self.assertEqual(count_words(""), 0)

    def test_non_string(self):
        self.assertEqual(count_words(None), 0)


if __name__ == "__main__":
    unittest.main()
