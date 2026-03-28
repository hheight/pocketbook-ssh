import unittest

from style_text import style_text

class TestStyleText(unittest.TestCase):
    def test_red(self):
        text = "test"
        styled_text = style_text(text, "red")

        self.assertEqual(
            styled_text,
            f"\033[31m{text}\033[0m"
         )

    def test_green(self):
        text = "test"
        styled_text = style_text(text, "green")

        self.assertEqual(
            styled_text,
            f"\033[32m{text}\033[0m"
         )

    def test_yellow(self):
        text = "test"
        styled_text = style_text(text, "yellow")

        self.assertEqual(
            styled_text,
            f"\033[33m{text}\033[0m"
         )

    def test_blue(self):
        text = "test"
        styled_text = style_text(text, "blue")

        self.assertEqual(
            styled_text,
            f"\033[34m{text}\033[0m"
         )

    def test_bold(self):
        text = "test"
        styled_text = style_text(text, "bold")

        self.assertEqual(
            styled_text,
            f"\033[1m{text}\033[0m"
         )

    def test_default(self):
        text = "test"
        styled_text = style_text(text, "default")

        self.assertEqual(
            styled_text,
            text
         )
