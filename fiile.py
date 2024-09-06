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
                result[field_name]['item.raw'].append(item['raw'])
                if 'component' in item:
                    for comp in item['component']:
                        comp_name, comp_value = comp
                        result[field_name][f'item.component.{comp_name}'].append(comp_value)
    return result

def save_to_csv(flat_data, filename):
    print(f"Saving to {filename}")  # Debugging line
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Key', 'Value'])
        for key, values in flat_data.items():
            for sub_key, sub_values in values.items():
                for value in sub_values:
                    print(f"  Writing: {key}.{sub_key} = {value}")  # Debugging line
                    writer.writerow([f'{key}.{sub_key}', value])
