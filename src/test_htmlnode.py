import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        properties_string = ' class="main-paragraph" align="center"'
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
        leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node2.to_html(), '<a href="https://www.google.com">Click me!</a>')    
        self.assertEqual(leaf_node.to_html(), "<p>I am a paragraph</p>")

    def test_to_html_without_a_tag(self):
        leaf_node = LeafNode(None, "I'm a value without tags")
        self.assertEqual(leaf_node.to_html(), "I'm a value without tags")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("b", "Bold text")
        child_node2 = LeafNode(None, "Normal text")
        child_node3 = LeafNode("i", "italic text")
        child_node4 = LeafNode(None, "Normal text")
        parent_node = ParentNode("p", [child_node1, child_node2, child_node3, child_node4])
        self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("p", None)
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(context.exception.args[0], "This object doesn't have children.")


if __name__ == "__main__":
    unittest.main()
