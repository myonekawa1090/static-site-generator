import textnode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    print("Hello, World!")
    tn = textnode.TextNode("This is some text", textnode.TextType.URL, "http://example.com")
    tn.__repr__()
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case textnode.TextType.NORMAL:
            return LeafNode(value=text_node.text)
        case textnode.TextType.ITALIC:
            return LeafNode("i", value=text_node.text)
        case textnode.TextType.BOLD:
            return LeafNode("b", value=text_node.text)
        case textnode.TextType.CODEBLOCK:
            return LeafNode("code", value=text_node.text)
        case textnode.TextType.URL:
            return LeafNode("a", value=text_node.text, props={"href": text_node.url})
        case textnode.TextType.IMAGE:
            return LeafNode("img", value=None, props={"src": text_node.url, "alt": str(text_node.text)})
        case _:
            raise ValueError(f"Unsupported TextType: {text_node.text_type}")
    
if __name__ == "__main__":
    main()