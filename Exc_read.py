from asyncore import read
import imp
import csv

def reader_excel():
    with open('Telephon_book.csv', 'r', encoding='utf-8') as con:
        reader_cont = csv.DictReader(con)
        for cont in reader_cont:
            print()
            for c in cont:
                print(c, cont[c])
