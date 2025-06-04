from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_list_strings = []
            strings = node.text.split(delimiter)
            if len(strings) % 2 == 0:
                raise ValueError("missing closing delimiter")
            if strings[0] == "":
                tag = 1 # starts with delimiter node
            else:
                tag = 0 # starts with text node
            for string in strings:
                if string == "":
                    pass
                elif tag == 0: # is text node
                    new_node = TextNode(string, TextType.TEXT)
                    node_list_strings.append(new_node)
                    tag = 1
                elif tag == 1: # is delimiter node
                    new_node = TextNode(string, text_type)
                    node_list_strings.append(new_node)
                    tag = 0
            new_nodes.extend(node_list_strings)
    return new_nodes