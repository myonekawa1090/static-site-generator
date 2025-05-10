import textnode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    print("Hello, World!")
    tn = textnode.TextNode("This is some text", textnode.TextType.LINK, "http://example.com")
    tn.__repr__()
    
if __name__ == "__main__":
    main()