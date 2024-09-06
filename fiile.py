def flatten_json(nested_json, parent_key='', sep='.'):
    items = []
    
    if isinstance(nested_json, list):
        # Obsługa listy, np. [["50k": {...}], ["4k": {...}]]
        for idx, element in enumerate(nested_json):
            if isinstance(element, list):
                for sub_element in element:
                    for k, v in sub_element.items():
                        new_key = f"{parent_key}{sep}{k}" if parent_key else k
                        if isinstance(v, dict):
                            items.extend(flatten_json(v, new_key, sep=sep).items())
            else:
                items.extend(flatten_json(element, parent_key, sep=sep).items())
    
    elif isinstance(nested_json, dict):
        # Obsługa słownika
        for k, v in nested_json.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_json(v, new_key, sep=sep).items())
            elif isinstance(v, list) and all(isinstance(i, list) for i in v):
                # Obsługa list komponentów
                for comp in v:
                    comp_key = f"{new_key}.component.{comp[0]}"
                    items.append((comp_key, comp[1]))
            else:
                items.append((new_key, v))
    else:
        # Obsługa wartości końcowych (liści)
        items.append((parent_key, nested_json))
    
    return dict(items)

# Iteracja przez dane JSON i spłaszczenie struktury
flattened_keys = set()  # Zbiór, aby zebrać wszystkie unikalne klucze

for idx, entry in data.items():
    for field in entry["field"]:
        flattened = flatten_json(field)  # Spłaszczamy każdy element w liście "field"
        flattened_keys.update(flattened.keys())  # Dodajemy klucze do zbioru

# Konwersja zbioru kluczy na posortowaną listę, aby stworzyć nagłówki
headers = sorted(flattened_keys)

# Wyświetlamy automatycznie wygenerowane nagłówki
print(headers)
