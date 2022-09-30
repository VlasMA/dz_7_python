import view as v
import csv
import os.path   #стандартная библ, можно обращаться к файлам

def writer_excel():
    if os.path.isfile('Telephon_book.csv'):
        with open('Telephon_book.csv', 'a', encoding='utf-8') as con:
            fieldnames = ['Number', 'Name', 'Surname', 'Text']
            writer = csv.DictWriter(con, fieldnames=fieldnames, restval='None')
            writer.writerow(v.new_contact())
    if not os.path.isfile('Telephon_book.csv'):
        with open('Telephon_book.csv', 'a', encoding='utf-8') as con:
            fieldnames = ['Number', 'Name', 'Surname', 'Text']
            writer = csv.DictWriter(con, fieldnames=fieldnames, restval='None')
            writer.writeheader()
            writer.writerow(v.new_contact())