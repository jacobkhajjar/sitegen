from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code block"
    QUOTE = "quote block"
    ULIST = "unordered list"
    OLIST = "ordered list"

def block_to_block_type(block):
    if bool(re.fullmatch(r"^#{1,6} .*", block)):
        return BlockType.HEADING
    if bool(re.fullmatch(r"`{3}\n*.*?\n*`{3}", block)):
        return BlockType.CODE
    if starts_with(block, ">"):
        return BlockType.QUOTE
    if starts_with(block, "- "):
        return BlockType.ULIST
    if starts_with(block, 1):
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH
    
def starts_with(block, delimiter):
    lines = block.split("\n")
    for line in lines:
        if isinstance(delimiter, int):
             if not line.startswith(f"{delimiter}. "):
                  return False
             delimiter += 1
        else:
            if not line.startswith(delimiter):
                return False
    return True

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = list(filter(lambda x: x != "", blocks))
    return blocks
