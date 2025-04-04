from textnode import TextNode, TextType, text_node_to_html_node


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            splitted_list = node.text.split(delimiter)
            if (len(splitted_list) % 2 == 0):
                raise ValueError("The matching closing delimiter is not found!")
            else:
                processed_nodes = []
                for i in range(0, len(splitted_list)):
                    if (splitted_list[i] == ""):
                        continue
                    elif (i % 2 == 0):
                        processed_nodes.append(TextNode(splitted_list[i], TextType.TEXT))
                    else:
                        processed_nodes.append(TextNode(splitted_list[i], text_type))
                new_nodes.extend(processed_nodes)
    return new_nodes
