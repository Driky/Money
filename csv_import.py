# -*-coding:Utf-8 -*

import csv

__author__ = 'Driky'

def import_csv_file(file):

    with open(file) as csvfile:

        reader = csv.reader(csvfile, delimiter=';', quotechar='|')


        first_row = 0

        for row in reader:
            if first_row == 0:
                tab = row.split(',')
                print(row)

            first_row = False
