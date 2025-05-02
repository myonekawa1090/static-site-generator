import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("", TextType.NORMAL)
        node5 = TextNode("%%%", TextType.URL)
        node6 = TextNode(3, TextType.IMAGE, "http://example.com/image.png")
        node7 = TextNode(["a", "b", "c"], TextType.NORMAL, "http://example.com/list.png")
        node8 = TextNode({"a":"3"}, TextType.CODEBLOCK, "http://example.com")
        
        # Assertions
        self.assertEqual(node, node2)  # Same content and type
        self.assertNotEqual(node, node3)  # Different type
        self.assertNotEqual(node, node4)  # Different content
        self.assertNotEqual(node, node5)  # Different content and type
        self.assertNotEqual(node6, node7)  # Different content and type
        self.assertNotEqual(node7, node8)  # Different content and type

if __name__ == "__main__":
    unittest.main()