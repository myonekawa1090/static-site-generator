from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, TextNode):
        return (self.text == TextNode.text and
                self.text_type == TextNode.text_type and
                self.url == TextNode.url)
        
    def __repr__(self): 
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", value=text_node.text)
        case TextType.BOLD:
            return LeafNode("b", value=text_node.text)
        case TextType.CODE:
            return LeafNode("code", value=text_node.text)
        case TextType.LINK:
            return LeafNode("a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", value=None, props={"src": text_node.url, "alt": str(text_node.text)})
        case _:
            raise ValueError(f"Unsupported TextType: {text_node.text_type}")  
        