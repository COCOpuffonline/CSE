import csv
total = 0
div = 0


with open("Sales Records.csv", 'r') as old_csv:
    print("Reading File...   ")
    reader = csv.reader(old_csv)
    for row in reader:
        if row[2] == "Snacks":
            total += float(row[13])
            div += 1
            Av = total / div
print("The total profit of snacks is %s." % total)
print("Snacks appeared %s times." % div)
print("Average = %s" % Av)

