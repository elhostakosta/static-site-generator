import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_none_values(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_non_none_values(self):
        child = HTMLNode("span", "short text")
        properties = {"class": "main-paragraph", "align": "center"}
        parent = HTMLNode("p", "I am a text inside a paragraph", [child], properties)
        self.assertEqual(parent.tag, "p")
        self.assertEqual(parent.value, "I am a text inside a paragraph")
        self.assertEqual(parent.children, [child])
        self.assertEqual(parent.props, properties)

    def test_props_to_html_with_value(self):
        properties = {"class": "main-paragraph", "align": "center"}
        html_node = HTMLNode()
        html_node.props = properties
        properties_string = 'class="main-paragraph" align="center"'
        self.assertEqual(html_node.props_to_html(), properties_string)

    def test_props_to_html_without_value(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(), "")

    def test_repr(self):
        child = HTMLNode("span", "short text")
        properties = {"class": "main-paragraph", "align": "center"}
        parent = HTMLNode("p", "I am a text inside a paragraph", [child], properties)
        repr_string = f"*****\ntag: p\nvalue: I am a text inside a paragraph\nchildren: {[child]}\nprops: {properties}\n*****"
        self.assertEqual(repr_string, repr(parent))

    def test_to_html_with_leaf_node(self):
        leaf_node = LeafNode("p", "I am a paragraph")
        self.assertEqual(leaf_node.to_html(), "<p>I am a paragraph</p>")

    def test_to_html_without_a_tag(self):
        leaf_node = LeafNode(None, "I'm a value without tags")
        leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node2.to_html(), '<a href="https://www.google.com">Click me!</a>')
        self.assertEqual(leaf_node.to_html(), "I'm a value without tags")

if __name__ == "__main__":
    unittest.main()
