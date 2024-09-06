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
                result[field_name]['item.raw'].append(item.get('raw', ''))
                
                if 'component' in item:
                    for comp in item['component']:
                        if len(comp) == 2:  # Ensure each component has exactly 2 elements
                            comp_name, comp_value = comp
                            result[field_name][f'item.component.{comp_name}'].append(comp_value)
    
    return result

# Funkcja do zapisywania danych do pliku CSV w formacie tabelarycznym
def save_to_csv(flat_data, filename):
    print(f"Saving to {filename}")  # Debugging line
    
    # Kolekcjonowanie nagłówków i wartości
    headers = set()
    rows = defaultdict(list)
    
    for field_name, fields in flat_data.items():
        for sub_key, values in fields.items():
            headers.add(sub_key)
            for i, value in enumerate(values):
                rows[i].append(value)
    
    # Sortowanie nagłówków
    headers = sorted(headers)
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Zapis nagłówków
        writer.writerow(headers)
        
        # Zapis wartości wierszy
        for i in range(len(rows)):
            writer.writerow(rows[i])

# Przetwórz dane i zapisz do plików CSV
flat_data = flatten_data_for_all_keys(data)

# Zapisywanie danych do plików CSV
for field_name, data_dict in flat_data.items():
    filename = f'{field_name}.csv'
    save_to_csv(data_dict, filename)
    print(f'CSV file created: {filename}')
