import csv
total = 0
div = 0


with open("Sales Records.csv", 'r') as old_csv:
    print("Reading File...   ")
    reader = csv.reader(old_csv)
    category_list = []
    cereal = 0
    baby_food = 0
    vegetables = 0
    household = 0
    personal_care = 0
    snacks = 0
    cosmetics = 0
    office_supplies = 0
    meat = 0
    fruits = 0
    clothes = 0
    beverages = 0

    for row in reader:
        if row[2] == "Cereal":
            div += 1
            Av1 = cereal / div
            cereal += float(row[13])
        if row[2] == "Baby Food":
            div += 1
            Av2 = baby_food / div
            baby_food += float(row[13])
        if row[2] == "Vegetables":
            div += 1
            Av3 = vegetables / div
            vegetables += float(row[13])
        if row[2] == "Household":
            div += 1
            Av4 = household / div
            household += float(row[13])
        if row[2] == "Personal Care":
            div += 1
            Av5 = personal_care / div
            personal_care += float(row[13])
        if row[2] == "Snacks":
            div += 1
            Av6 = snacks / div
            snacks += float(row[13])
        if row[2] == "Cosmetics":
            div += 1
            Av7 = cosmetics / div
            cosmetics += float(row[13])
        if row[2] == "Office Supplies":
            div += 1
            Av8 = office_supplies / div
            office_supplies += float(row[13])
        if row[2] == "Meat":
            div += 1
            Av9 = meat / div
            meat += float(row[13])
        if row[2] == "Fruits":
            div += 1
            Av10 = fruits / div
            fruits += float(row[13])
        if row[2] == "Clothes":
            div += 1
            Av11 = clothes / div
            clothes += float(row[13])
        if row[2] == "Beverages":
            div += 1
            Av12 = beverages / div
            beverages += float(row[13])
print("Cereal = %s" % Av1)
