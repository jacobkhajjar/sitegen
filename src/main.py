from textnode import TextNode, TextType

def main():
    test = TextNode("this is text", TextType.LINK, "thisisaurl")
    print(test)

main()