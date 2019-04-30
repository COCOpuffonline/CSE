def all_16_digits(num: str):
    if len(num) == 16:
        print(num)
        return True


def drop_num(num: str):
    list_num = list(num)
    for index in range(len(list_num)):
        list_num[index] = int(list_num[index])
        list_num.remove(15)
        print(list_num)


def validate


print(1947333886071750)

# def reverse_it(number_list):
#     print(number_list[17:0:-1])
#
#     reverse_it(number_list)


# def reverse_it(string):
#     print(string[17:0:-1])
#
#     reverse_it(string)


# # The Luhn Formula:
# #
# # Drop the last digit from the number. The last digit is what we want to check against
# # Reverse the numbers
# # Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# # Add all the numbers together
# # The check digit (the last number of the card)
# is the amount that you would need to add to get a multiple of 10 (Modulo 10)
