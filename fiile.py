def flatten_data(data):
    flat_dict = {}
    
    for key, value in data.items():
        for field in value["field"]:
            field_name = field[0]
            field_data = field[1]
            
            if 'item' in field_data:
                item = field_data['item'][0]
                
                # Przypisz raw value
                flat_dict[f'{field_name}.item.raw'] = item['raw']
                
                # Przypisz component values
                if 'component' in item:
                    for comp in item['component']:
                        comp_name, comp_value = comp
                        flat_dict[f'{field_name}.item.component.{comp_name}'] = int(comp_value)
    
    return flat_dict

# Generowanie płaskiego słownika
flat_data = flatten_data(data)
