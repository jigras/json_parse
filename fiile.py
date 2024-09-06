import csv
from collections import defaultdict



def flatten_data_for_all_keys(data):
    result = defaultdict(lambda: defaultdict(list))

    for key, value in data.items():
        for field in value["field"]:
            field_name = field[0]
            field_data = field[1]

            if 'item' in field_data and field_data['item']:
                item = field_data['item'][0]
                result[field_name]['item.raw'].append(item.get('raw', ''))

                if 'component' in item:
                    for comp in item['component']:
                        if len(comp) == 2:  #
                            comp_name, comp_value = comp
                            result[field_name][f'item.component.{comp_name}'].append(comp_value)

    return result



flat_data = flatten_data_for_all_keys(data)


# Przetwórz dane i zapisz do plików CSV
def save_to_txt(data_dict, filename):
    headers = list(data_dict.keys())
    num_rows = max(len(data_dict[header]) for header in headers)

    with open(filename, 'w') as txtfile:

        header_line = ','.join(headers) + '\n'
        txtfile.write(header_line)


        for i in range(num_rows):
            row = [data_dict[header][i] if i < len(data_dict[header]) else '' for header in headers]
            row_line = ','.join(map(str, row)) + '\n'
            txtfile.write(row_line)


for key, data_dict in flat_data.items():
    filename = f'{key}.txt'
    save_to_txt(data_dict, filename)
    print(f'TXT file created: {filename}')
