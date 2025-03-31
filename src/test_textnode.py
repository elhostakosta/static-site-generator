import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.text, "This is a text node")
        
        
    def test_url(self):
        node = TextNode("Not you again!", TextType.LINK, "https://example.com/")
        node2 = TextNode("Who am I?", TextType.LINK)
        self.assertEqual(None, node2.url)
        self.assertEqual(node.url, "https://example.com/")

    def test_non_eq(self):
        node1 = TextNode("We have the same text!", TextType.LINK)
        node2 = TextNode("We have the same text!", TextType.ITALIC)
        node3 = TextNode("Tommy", TextType.LINK)
        node4 = TextNode("Trevor", TextType.LINK)
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node3, node4)

    def test_repr(self):
        node = TextNode("I'm a text node", TextType.ITALIC, "https://example.com/")
        node2 = TextNode("I'm a text node", TextType.ITALIC)
        self.assertEqual(repr(node), "TextNode(I'm a text node, italic, https://example.com/)")
        self.assertEqual(repr(node2), "TextNode(I'm a text node, italic, None)")

class TestConvertingTextNodeToHtmlNode(unittest.TestCase):
    def test_to_html_node_with_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.text, "This is a text node")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()
