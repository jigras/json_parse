def flatten_data_for_all_keys(data):
    result = defaultdict(lambda: defaultdict(list))

    for key, value in data.items():
        print(f"Processing key: {key}")  # Debugging line
        for field in value["field"]:
            field_name = field[0]
            field_data = field[1]
            print(f"  Field: {field_name}")  # Debugging line
            
            if 'item' in field_data and field_data['item']:
                item = field_data['item'][0]
                print(f"    Raw: {item.get('raw', 'No raw value')}")
                result[field_name]['item.raw'].append(item.get('raw', 'No raw value'))
                
                if 'component' in item:
                    for comp in item['component']:
                        if len(comp) == 2:  # Ensure each component has exactly 2 elements
                            comp_name, comp_value = comp
                            result[field_name][f'item.component.{comp_name}'].append(comp_value)
                        else:
                            print(f"    Invalid component format: {comp}")
            else:
                print(f"  No 'item' key or 'item' is empty for field: {field_name}")
    
    return result

# Funkcja do zapisywania danych do pliku CSV
def save_to_csv(flat_data, filename):
    print(f"Saving to {filename}")  # Debugging line
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Key', 'Value'])
        for key, values in flat_data.items():
            print(f"  Processing field: {key}")  # Debugging line
            if isinstance(values, dict):
                for sub_key, sub_values in values.items():
                    print(f"    Sub-key: {sub_key}")  # Debugging line
                    if isinstance(sub_values, list):
                        for value in sub_values:
                            print(f"      Writing: {key}.{sub_key} = {value}")  # Debugging line
                            writer.writerow([f'{key}.{sub_key}', value])
                    else:
                        print(f"    Unexpected format for sub-values: {sub_values}")
            else:
                print(f"  Unexpected format for values: {values}")

# Przetwórz dane i zapisz do plików CSV
flat_data = flatten_data_for_all_keys(data)

# Zapisywanie danych do plików CSV
for field_name, data_dict in flat_data.items():
    filename = f'{field_name}.csv'
    save_to_csv(data_dict, filename)
    print(f'CSV file created: {filename}')
