import unittest

from htmlnode import HTMLNode, LeafNode


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

if __name__ == "__main__":
    unittest.main()