import re

from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextType, TextNode

def markdown_to_html_node(markdown):
    final_children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                text = block.lstrip("#").lstrip()
                heading = ParentNode(heading_count(block), text_to_children(text))
                final_children.append(heading)
            case BlockType.CODE:
                text = block[4:-3]
                text_node = TextNode(text, TextType.TEXT)
                code_child = text_node_to_html_node(text_node)
                code_block = ParentNode("code", [code_child])
                code_node = ParentNode("pre", [code_block])
                final_children.append(code_node)
            case BlockType.QUOTE:
                text = clean_quote(block)
                quote = ParentNode("blockquote", text_to_children(text))
                final_children.append(quote)
            case BlockType.ULIST:
                ulist = ParentNode("ul", list_tag(block))
                final_children.append(ulist)
            case BlockType.OLIST:
                olist = ParentNode("ol", list_tag(block))
                final_children.append(olist)
            case BlockType.PARAGRAPH:
                lines = block.split("\n")
                text = " ".join(lines)
                paragraph = ParentNode("p", text_to_children(text))
                final_children.append(paragraph)
    final_html = ParentNode("div", final_children)
    return final_html

def text_to_children(text):
    return list(map(text_node_to_html_node, (text_to_textnodes(text))))

def heading_count(block):
    if block.startswith("# "):
        return "h1"
    if block.startswith("## "):
        return "h2"
    if block.startswith("### "):
        return "h3"
    if block.startswith("#### "):
        return "h4"
    if block.startswith("##### "):
        return "h5"
    if block.startswith("###### "):
        return "h6"
    else:
        raise ValueError("invalid heading tag")
    
def clean_quote(block):
    clean = []
    lines = block.split("\n")
    for line in lines:
        clean.append(line.lstrip(">").strip())
    return " ".join(clean)

def list_tag(block):
    list_nodes = []
    lines = block.split("\n")
    if block.startswith("-"):
        stripped_lines = list(map(lambda x: x.lstrip("- "), lines))
    else:
        stripped_lines = list(map(lambda x: re.sub(r"\d+\. ", "", x, 1), lines))
    for line in stripped_lines:
        children = text_to_children(line)
        list_nodes.append(ParentNode("li", children))
    return list_nodes