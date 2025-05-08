
class HTMLNode: 
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self): 
        raise NotImplementedError()
    
    def props_to_html(self): 
        if self.props is None: 
            return ""
        
        props_str = ""
        for key, value in self.props.items(): 
            if isinstance(value, str): 
                props_str += f'{key}="{value}" '
            elif isinstance(value, list): 
                props_str += f' {key}="{" ".join(value)}"'
            else: 
                raise ValueError(f"Unsupported prop type: {type(value)}")
        return props_str
 
    def __repr__(self): 
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        
class LeafNode(HTMLNode): 
    def __init__(self, tag=None, value=None, props=None): 
        super().__init__(tag, value, None, props)
        
    def to_html(self): 
        if self.value is None: 
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None: 
            return self.value
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode): 
    def __init__(self, tag, children, props=None): 
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self):
        if self.tag is None: 
            raise ValueError("ParentNode tag cannot be None")
        if self.children is None: 
            raise ValueError("ParentNode children cannot be None")
        props_str = self.props_to_html()
        children_str = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{props_str}>{children_str}</{self.tag}>"
