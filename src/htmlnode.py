
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
                props_str += f' {key}="{" ".jo  in(value)}"'
            else: 
                raise ValueError(f"Unsupported prop type: {type(value)}")
        return props_str
 
    def __repr__(self): 
        print(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")