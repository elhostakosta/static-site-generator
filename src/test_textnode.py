import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node.text, "This is a text node")

    def test_url(self):
        node = TextNode("I am a text node", text_type_bold)
        node2 = TextNode("I am also a text node", text_type_bold, "https://example.com/")
        self.assertEqual(node.url, None)
        self.assertEqual(node2.url, "https://example.com/")

    def test_text_type(self):
        node = TextNode("A text node", text_type_bold)
        self.assertEqual(node.text_type, text_type_bold)

    def test_non_eq(self):
        node1 = TextNode("First text node", text_type_italic)
        node2 = TextNode("Second text node", text_type_bold)
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("I'm a text node", text_type_italic, "https://chatgpt.com/")
        self.assertEqual(repr(node), "TextNode(I'm a text node, italic, https://chatgpt.com/)")

if __name__ == "__main__":
    unittest.main()
