"""
program: new_ticket.py
Author: Zhe Zhang A01257572 Set B
Date: Apr 22 2021
"""

import datetime
from csv import reader

def get_info():
    email = input('Enter your email address: ')
    desc = input('Enter a short description (60 chars max):\n')

    return email, desc


def create_new_str(email, desc, file):
    new_list = []
    total_data = []
    with open(file, 'r') as f:
        content = f.readlines()
        for i in content:
            for line in reader([i.strip()]):
                person_data = line
            total_data.append(person_data)
    new_num = int(total_data[len(total_data) - 1][0]) + 1
    new_time = datetime.datetime.now()
    new_status = 'Pending'
    new_list = [f"{new_num},{new_time},{email},,,{desc},,{new_status}"]

    return '\n'.join(new_list), new_num


def write_into_csv(string, file, new_num, desc):
    with open(file, 'a') as f:
        f.write(f'{string}\n')
    
    return f'Ticket #{new_num} ({desc}) created.'

def main():
    file_name = 'tickets.csv'
    print('Create New Trouble Ticket\n=========================')
    email, description = get_info()
    while len(description) not in range(10, 60):
        if len(description) < 10:
            print('** the description must contain at least 10 characters')
            description = input('Enter a short description (60 chars max):\n')
        elif len(description) > 60:
            print('** the description must contain at most 60 characters')
            description = input('Enter a short description (60 chars max):\n')
    new_string, new_num = create_new_str(email, description, file_name)
    result = write_into_csv(new_string, file_name, new_num, description)
    print(result)


main()
