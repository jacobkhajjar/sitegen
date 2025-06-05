from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_list_sections = []
            sections = node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise ValueError("missing closing delimiter")
            if sections[0] == "":
                tag = 1 # starts with delimiter node
            else:
                tag = 0 # starts with text node
            for section in sections:
                if section == "":
                    pass
                elif tag == 0: # is text node
                    new_node = TextNode(section, TextType.TEXT)
                    node_list_sections.append(new_node)
                    tag = 1
                elif tag == 1: # is delimiter node
                    new_node = TextNode(section, text_type)
                    node_list_sections.append(new_node)
                    tag = 0
            new_nodes.extend(node_list_sections)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_list_sections = []
        image_count = len(extract_markdown_images(node.text))
        if image_count == 0:
            new_nodes.append(node)
        else:
            current_text = node.text
            while image_count >= 0:
                if image_count > 0:
                    images = extract_markdown_images(current_text)
                    image_alt = images[0][0]
                    image_link = images[0][1]
                    sections = current_text.split(f"![{image_alt}]({image_link})", 1)
                    if len(sections) != 2:
                        raise ValueError("invalid markdown, image section not closed")
                    if sections[0] == "": # starts with image
                        new_node = TextNode(image_alt, TextType.IMAGE, image_link)
                        node_list_sections.append(new_node)
                        if sections[1] != "":
                            new_node = TextNode(sections[1], TextType.TEXT)
                            node_list_sections.append(new_node)
                    else: # starts with text
                        new_node = TextNode(sections[0], TextType.TEXT)
                        node_list_sections.append(new_node)
                        new_node = TextNode(image_alt, TextType.IMAGE, image_link)
                        node_list_sections.append(new_node)
                    current_text = sections[1]
                    image_count = len(extract_markdown_images(current_text))
                if image_count == 0: # trailing text
                    if current_text != "":
                        new_node = TextNode(current_text, TextType.TEXT)
                        node_list_sections.append(new_node)
                    image_count = -1 # exit loop
        new_nodes.extend(node_list_sections)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        node_list_sections = []
        link_count = len(extract_markdown_links(node.text))
        if link_count == 0:
            new_nodes.append(node)
        else:
            current_text = node.text
            while link_count >= 0:
                if link_count > 0:
                    links = extract_markdown_links(current_text)
                    link_alt = links[0][0]
                    link_url = links[0][1]
                    sections = current_text.split(f"[{link_alt}]({link_url})", 1)
                    if len(sections) != 2:
                        raise ValueError("invalid markdown, image section not closed")
                    if sections[0] == "": # starts with link
                        new_node = TextNode(link_alt, TextType.LINK, link_url)
                        node_list_sections.append(new_node)
                        if sections[1] != "":
                            new_node = TextNode(sections[1], TextType.TEXT)
                            node_list_sections.append(new_node)
                    else: # starts with text
                        new_node = TextNode(sections[0], TextType.TEXT)
                        node_list_sections.append(new_node)
                        new_node = TextNode(link_alt, TextType.LINK, link_url)
                        node_list_sections.append(new_node)
                    current_text = sections[1]
                    link_count = len(extract_markdown_links(current_text))
                if link_count == 0: # trailing text
                    if current_text != "":
                        new_node = TextNode(current_text, TextType.TEXT)
                        node_list_sections.append(new_node)
                    link_count = -1 # exit loop
        new_nodes.extend(node_list_sections)
    return new_nodes



node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another", TextType.TEXT)
print (split_nodes_image([node]))