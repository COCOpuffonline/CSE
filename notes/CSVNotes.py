import csv


def validate(num: str):
    if all_16_digits(num):
        return False
    if divisilbe_by_2(num) and divisilbe_by_3(num):
        return True
    return False


def divisilbe_by_3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisilbe_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


def all_16_digits(num: str):
    if len(num) == 16:
        return True
    else:
        print("NOT EVERY NUMBER IS 16 DIGITS!!!!")


# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print("Writing File...   ")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#             old_number = row[0]  # This is a string
#             first_num = int(old_number[0])  # This is the first
#             if first_num % 2 == 0:
#                 writer.writerow(row)
#             # print_int(old_number) + 1)
#             # print(old_number)
# print("OK")

def reverse_it(string):
    print(string[11:0:-1])


reverse_it("Hello World")


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing File...   ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]  # This is a string
            if validate(old_number):
                writer.writerow(row)
print("Done")


def valid_card_number(num: str):

    print(valid_card_number("2765980325287548"))


list_number = list(number)
for index in range(len(list_number)):
    list_number[index] = int(list_number[index])

