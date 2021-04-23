"""
program: show_tickets.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 22 2021
"""

import sys
from csv import reader


def read_file(file):
    total_data = []
    with open(file, 'r') as f:
        content = f.readlines()
        for i in content:
            for line in reader([i.strip()]):
                person_data = line
            total_data.append(person_data)

    return total_data


def arrange_data(data, dict_data):
    new_data = []
    final_data = []
    for i, value in enumerate(data[:]):
        if data[i][4] != '':
            data[i][4] = dict_data[data[i][4]]
        if data[i][6] != '':
            data[i][6] = dict_data[data[i][6]]
    for i in data:
        new_data.append(f'{i[0]:3}')
        new_data.append(f'{i[1][:10]:11}')
        new_data.append(f'{i[6]:9}')
        new_data.append(f'{i[7]:9}')
        new_data.append(f'{i[3]:9}')
        new_data.append(f'{i[4]:9}')
        new_data.append(f'{i[5][:40]:41}')
        new_data.append(i[2])
        final_data.append(new_data)
        new_data = []

    return final_data


def display_data(data):
    result = []
    for i in data:
        data_str = ' '.join(i)
        result.append(data_str)

    return '\n'.join(result)


def display_assigned(data, cmd):
    result = []
    for i in data:
        if i[3] == f'{cmd:9}':
            data_str = ' '.join(i)
            result.append(data_str)

    return '\n'.join(result)


def main():
    try:
        dict_data = {'H': 'Hardware', 'S': 'Software', 'N': 'Network', 'L': 'Login', 'O': 'Other',
                '1': 'Urgent', '2': 'High', '3': 'Normal', '4': 'Low'}
        file_name = 'tickets.csv'
        total_data = read_file(file_name)
        final_data = arrange_data(total_data, dict_data)
        cmd = sys.argv[1]
        if cmd == 'Assigned':
            result = display_assigned(final_data, cmd)
            print('ID  Created     Priority  Status    Assigned  Type      Title                                     Submitted By')
            print('--  ----------  --------  --------  --------  --------  ----------------------------------------  ------------------------')
            print(result)
        else:
            result = f'Error: {cmd} is invalid command!'
            print(result)
    except IndexError:
        result = display_data(final_data)
        print('ID  Created     Priority  Status    Assigned  Type      Title                                     Submitted By')
        print('--  ----------  --------  --------  --------  --------  ----------------------------------------  ------------------------')
        print(result)
    except FileNotFoundError:
        sys.exit(f'Error: {file_name} is not exist.')


main()