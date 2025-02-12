"""
Extracts data, from a POD
"""

import ast

def extract(code):
    # Parse the code into an abstract syntax tree (AST)
    tree = ast.parse(code)
    
    data = {}

    # Function to handle the AST nodes
    def handle_node(node):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    var_name = target.id
                    value = node.value
                    
                    # Handling different types of values (numbers, strings, lists, dicts, etc.)
                    if isinstance(value, ast.Str):
                        data[var_name] = f'"{value.s}"'
                    elif isinstance(value, ast.Num):
                        data[var_name] = value.n
                    elif isinstance(value, ast.List):
                        elements = [handle_node(e) for e in value.elts]
                        data[var_name] = f"[{', '.join(elements)}]"
                    elif isinstance(value, ast.Dict):
                        keys = [handle_node(k) for k in value.keys]
                        values = [handle_node(v) for v in value.values]
                        data[var_name] = f"{{{', '.join([f'{k}: {v}' for k, v in zip(keys, values)])}}}"
                    elif isinstance(value, ast.Tuple):
                        elements = [handle_node(e) for e in value.elts]
                        data[var_name] = f"({', '.join(elements)})"
                    elif isinstance(value, ast.Set):
                        elements = [handle_node(e) for e in value.elts]
                        data[var_name] = f"{{{', '.join(elements)}}}"
                    elif isinstance(value, ast.NameConstant):
                        data[var_name] = value.value
                    else:
                        data[var_name] = ast.dump(value)
        elif isinstance(node, ast.NameConstant):
            return str(node.value)
        elif isinstance(node, ast.Str):
            return f'"{node.s}"'
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Num):
            return str(node.n)
        elif isinstance(node, ast.List):
            elements = [handle_node(e) for e in node.elts]
            return f"[{', '.join(elements)}]"
        elif isinstance(node, ast.Tuple):
            elements = [handle_node(e) for e in node.elts]
            return f"({', '.join(elements)})"
        elif isinstance(node, ast.Set):
            elements = [handle_node(e) for e in node.elts]
            return f"{{{', '.join(elements)}}}"
        elif isinstance(node, ast.Dict):
            keys = [handle_node(k) for k in node.keys]
            values = [handle_node(v) for v in node.values]
            return f"{{{', '.join([f'{k}: {v}' for k, v in zip(keys, values)])}}}"
        return str(node)

    # Iterate through the nodes in the AST and extract data
    for node in tree.body:
        handle_node(node)

    return data
