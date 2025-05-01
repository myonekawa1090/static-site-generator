from enum import Enum

class TextType(Enum):
    Normaltext = 1
    Italictext = 2
    Codetext = 3
    linktext = 4
    imagetext = 5
    
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, TextNode1, TextNode2):
        return (TextNode1.text == TextNode2.text and
                TextNode1.text_type == TextNode2.text_type and
                TextNode1.url == TextNode2.url)
        
    def __repr__(self): 
        return print(f"TextNode({self.text}, {self.text_type.value}, {self.url})")
    
        