import csv

with open("Book1.csv") as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        # old_number = int(row)[0]) + 1
        old_number = int(row[0]) + 1
        print(old_number)
