import csv


with open("Sales Records.csv", 'r') as old_csv:
    print("Writing File...   ")
    reader = csv.reader(old_csv)
    for row in reader:
        row = row[13]
        print(row)

# with open("MyNewFile.csv", 'w', newline='') as new_csv:
