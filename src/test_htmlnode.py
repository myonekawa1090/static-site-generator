import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        nodes = []
        nodes.append(HTMLNode("div", "This is a text node", None, {"class": "text-node"}))
        nodes.append(HTMLNode("div", "This is a text node", None, {"class": "text-node"}))
        nodes.append(HTMLNode("span", "This is a text node", None, {"class": "text-node"}))
        nodes.append(HTMLNode("div", "", None, {"class": "text-node", "id": "text-node"}))
        nodes.append(HTMLNode("div", "%%%", None, {"class": "text-node"}))
        nodes.append(HTMLNode("img", 3, None, {"src": "http://example.com/image.png"}))
        nodes.append(HTMLNode("ul", ["a", "b", "c"], None, {"class": "text-node"}))
        nodes.append(HTMLNode("pre", {"a": "3"}, None, {"class": "text-node"}))

        # Assertions
        for i, node in enumerate(nodes): 
            print(f"testing node {i} ...:" + node.props_to_html())

    def test_leaf_node(self):
        node = LeafNode("p", "Hello, world!")
        print(f"testing Leaf Node...", self.assertEqual(node.to_html(), "<p>Hello, world!</p>"))
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        print(f"test_to_html ... {self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")}")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        print("testing test_to_html_with_grandchildren ...")
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()