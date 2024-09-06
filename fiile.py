def flatten_data_for_all_keys(data):
    result = defaultdict(lambda: defaultdict(list))

    for key, value in data.items():
        for field in value["field"]:
            field_name = field[0]
            field_data = field[1]
            
            if 'item' in field_data:
                item = field_data['item'][0]
                
                # Dodaj raw value
                result[field_name]['item.raw'].append(item['raw'])
                
                # Dodaj component values
                if 'component' in item:
                    for comp in item['component']:
                        comp_name, comp_value = comp
                        result[field_name][f'item.component.{comp_name}'].append(comp_value)
    
    return result

# Funkcja do zapisywania danych do pliku CSV
def save_to_csv(flat_data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Key', 'Value'])
        for key, values in flat_data.items():
            for sub_key, sub_values in values.items():
                for value in sub_values:
                    writer.writerow([f'{key}.{sub_key}', value])

# Przetwórz dane i zapisz do plików CSV
flat_data = flatten_data_for_all_keys(data)

for field_name, data_dict in flat_data.items():
    filename = f'{field_name}.csv'
    save_to_csv(data_dict, filename)
    print(f'CSV file created: {filename}')
