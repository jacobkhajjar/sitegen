from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    test = TextNode("this is text", TextType.LINK, "thisisaurl")
    print(test)

main()