def save_to_csv(data_dict, filename):
    # Pobierz nagłówki (klucze z wewnętrznego słownika)
    headers = list(data_dict.keys())
    
    # Sprawdź długość najdłuższej listy, aby ustalić liczbę wierszy
    num_rows = max(len(data_dict[header]) for header in headers)
    
    # Otwórz plik w trybie zapisu
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        # Zapisz nagłówki (jako nagłówki kolumn)
        writer.writerow(headers)
        
        # Zapisz wartości wierszy
        for i in range(num_rows):
            row = [data_dict[header][i] if i < len(data_dict[header]) else '' for header in headers]
            writer.writerow(row)

# Przetwórz dane i zapisz do plików CSV z rozszerzeniem .txt
for key, data_dict in data.items():
    filename = f'{key}.txt'
    save_to_csv(data_dict, filename)
    print(f'TXT file created: {filename}')
