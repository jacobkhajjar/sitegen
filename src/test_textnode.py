import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_n_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "this has a url")
        self.assertNotEqual(node, node2)
    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node with different text", TextType.LINK)
        self.assertNotEqual(node, node2)
    def test_texttype(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.LINK, "url here")
        node2 = TextNode("This is a text node", TextType.LINK, "url here")
        self.assertEqual(node, node2)
    


if __name__ == "__main__":
    unittest.main()