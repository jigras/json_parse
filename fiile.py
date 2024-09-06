def flatten_data_for_key(data, key):
    flat_dict = {}
    
    for field in data[key]["field"]:
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
                    flat_dict[f'{field_name}.item.component.{comp_name}'] = comp_value
    
    return flat_dict

# Funkcja do zapisywania danych do pliku CSV
def save_to_csv(flat_data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Key', 'Value'])
        for key, value in flat_data.items():
            writer.writerow([key, value])

# Przetwórz dane i zapisz do plików CSV
for key in data:
    flat_data = flatten_data_for_key(data, key)
    filename = f'output_{key}.csv'
    save_to_csv(flat_data, filename)
    print(f'CSV file created: {filename}')
