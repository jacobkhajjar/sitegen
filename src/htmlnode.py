# HTMLNode represents a "node" in an HTML document tree (like a <p> tag and its contents, or an <a> tag and its contents). It can be block level or inline, and is designed to only output HTML.

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
        # Child classes will override this method to render themselves as HTML.

    def props_to_html(self):
        if self.props is None:
            return ""
        prop_string = ""
        for key in self.props:
            value = self.props[key]
            prop_string += f' {key}="{value}"'
        return prop_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})" 
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf HTML nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("parent HTML nodes must have a tag")
        if self.children is None:
            raise ValueError("parent HTML nodes must have children")
        html = ""
        for child in self.children:
            html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        
        
