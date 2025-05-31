import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_base(self):
        node = HTMLNode("test tag", "test value", ["test", "children", "list"], {"test key 1": "test value 1", "test key 2": "test value 2"})
        print (f"base test: {node}")

    def test_nonevalue(self):
        node = HTMLNode(tag="test tag", children=["test", "children", "list"], props={"test key 1": "test value 1", "test key 2": "test value 2"})
        print (f"none value test: {node}")

    def test_props(self):
        node = HTMLNode(tag="test tag", children=["test", "children", "list"], props={"test key 1": "test value 1", "test key 2": "test value 2"})
        print (f"props to HTML test: {node.props_to_html()}")
    


if __name__ == "__main__":
    unittest.main()