import csv
total = 0
div = 0


with open("Sales Records.csv", 'r') as old_csv:
    print("Reading File...   ")
    reader = csv.reader(old_csv)
    item_list = []
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

item_list.append(cereal)
item_list.append(baby_food)
item_list.append(vegetables)
item_list.append(household)
item_list.append(personal_care)
item_list.append(snacks)
item_list.append(cosmetics)
item_list.append(office_supplies)
item_list.append(meat)
item_list.append(fruits)
item_list.append(clothes)
item_list.append(beverages)

print("Cereal profit is %s." % cereal)
print("Baby food profit is %s." % baby_food)
print("Vegetables profit is %s." % vegetables)
print("Household profit is %s." % household)
print("Personal profit is %s." % personal_care)
print("Snacks profit is %s." % snacks)
print("Cosmetics profit is %s." % cosmetics)
print("Office supplies profit is %s." % office_supplies)
print("Meat profit is %s." % meat)
print("Fruits profit is %s." % fruits)
print("Clothes profit is %s." % clothes)
print("Beverages profit is %s." % beverages)

def max_num(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max


print("The most profitable item made %s." % max_num(item_list))

