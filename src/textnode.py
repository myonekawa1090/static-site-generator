from enum import Enum

class TextType(Enum):
    NORMAL = 1
    ITALIC = 2
    BOLD = 3
    CODEBLOCK = 3
    URL = 4
    IMAGE = 5
    
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
        return print(f"TextNode({self.text}, {self.text_type.value}, {self.url})")
    
        