class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        html_attributes = ""

        if self.props == None:
            return html_attributes

        for prop in self.props:
            html_attributes += f' {prop}="{self.props[prop]}"'
        
        return f"{html_attributes}"

    def __repr__(self):
        return f"*****\ntag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}\n*****"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML")
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
            raise ValueError("This object doesn't have a tag.")
        elif self.children is None:
            raise ValueError("This object doesn't have children.")
        else:
            html_format = ""
            for child in self.children:
                html_format += child.to_html()

            return f"<{self.tag}>{html_format}</{self.tag}>"
