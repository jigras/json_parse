def flatten_for_key(nested_json, target_key='50k', parent_key='', sep='.'):
    items = []
    
    if isinstance(nested_json, list):
        for element in nested_json:
            if isinstance(element, list):
                for sub_element in element:
                    if target_key in sub_element:
                        new_key = f"{parent_key}{sep}{target_key}" if parent_key else target_key
                        items.extend(flatten_json(sub_element[target_key], new_key, sep=sep).items())
    
    return dict(items)

def flatten_json(nested_json, parent_key='', sep='.'):
    items = []
    
    if isinstance(nested_json, dict):
        for k, v in nested_json.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_json(v, new_key, sep=sep).items())
            elif isinstance(v, list) and all(isinstance(i, list) for i in v):
                for comp in v:
                    comp_key = f"{new_key}.component.{comp[0]}"
                    items.append((comp_key, comp[1]))
            else:
                items.append((new_key, v))
    
    return dict(items)

flattened_result = flatten_for_key(data[0]["field"], target_key='50k')

print(flattened_result)
