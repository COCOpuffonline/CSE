def all_16_digits(num: str):                    # Works
    if len(num) == 16:
        print(num)
        print("This is 16 digits.")
        return True
    else:
        print("This number does not have 16 digits.")


def drop_num(num: str):                         # Works
    list_num = list(num)
    for index in range(len(list_num)):
        list_num[index] = int(list_num[index])
        list_num.pop(15)
        return list_num


def reverse(num: str):                          # Works
    list_num = list(num)
    print(list_num[::-1])


def multiply(num: str):
    for i in range(len(num)):
        if num[i] % 2 != 0:
            print(num[i] * 2)


def validate(num: str):
    if not all_16_digits(num):
        drop_num(num)
    reverse(num)
    multiply(num)


# print(all_16_digits("1947333886071750"))
# print(drop_num("1947333886071750"))
# print(reverse("1947333886071750"))
print(multiply("1947333886071750"))



# # The Luhn Formula:
# #
# # Drop the last digit from the number. The last digit is what we want to check against
# # Reverse the numbers
# # Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# # Add all the numbers together
# # The check digit (the last number of the card)
# is the amount that you would need to add to get a multiple of 10 (Modulo 10)
