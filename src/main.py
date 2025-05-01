import textnode

def main():
    print("Hello, World!")
    tn = textnode.TextNode("This is some text", textnode.TextType.linktext, "http://example.com")
    tn.__repr__()
    
    
if __name__ == "__main__":
    main()