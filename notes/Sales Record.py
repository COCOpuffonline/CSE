import csv
snacks_profit = []


with open("Sales Records.csv", 'r') as old_csv:
    print("Reading File...   ")
    reader = csv.reader(old_csv)
    for row in reader:
        if row[2] == "Snacks":
            print(row[2])
            print(row[13])


# with open("MyNewFile.csv", 'w', newline='') as new_csv:
# Cereal, beverages, personal care, baby food, snacks, meat, household, cosmetics, vegetables, cloths, office supplies
# , fruits# def get_total():
# #     cereal_number == 0
# #     beverages_number == 0
# #     personal_care_number == 0
# #     baby_food_number == 0
# #     snacks_number == 0
# #     meat_number == 0
# #     household_number == 0
# #     cosemetics_number == 0
# #     vegetables_number == 0
# #     cloths_number == 0
# #     office_supplies_number == 0
# #     fruits_number == 0
# #
