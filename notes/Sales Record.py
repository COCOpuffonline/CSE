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
            cereal += float(row[13])
        if row[2] == "Baby Food":
            baby_food += float(row[13])
        if row[2] == "Vegetables":
            vegetables += float(row[13])
        if row[2] == "Household":
            household += float(row[13])
        if row[2] == "Personal Care":
            personal_care += float(row[13])
        if row[2] == "Snacks":
            snacks += float(row[13])
        if row[2] == "Cosmetics":
            cosmetics += float(row[13])
        if row[2] == "Office Supplies":
            office_supplies += float(row[13])
        if row[2] == "Meat":
            meat += float(row[13])
        if row[2] == "Fruits":
            fruits += float(row[13])
        if row[2] == "Clothes":
            clothes += float(row[13])
        if row[2] == "Beverages":
            beverages += float(row[13])


def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max


print(max_num_in_list(("%s, %s") % cereal , meat))


# print("Cereal profit = %s" % cereal)
# print("Baby food profit = %s" % baby_food)
# print("Vegetables profit = %s" % vegetables)
# print("Household profit = %s" % household)
# print("Personal care profit = %s" % personal_care)
# print("Snacks profit = %s" % snacks)
# print("Cosmetics profit = %s" % cosmetics)
# print("Office supplies profit = %s" % office_supplies)
# print("Meat profit = %s" % meat)
# print("Fruit profit = %s" % fruits)
# print("Clothes profit = %s" % clothes)
# print("Beverages profit = %s" % beverages)
