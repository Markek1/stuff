num_of_numbers = int(input("How many numbers:"))
exponent = int(input("Exponent: "))


def calculate_spaces(longest_number, current_number):
    number_of_spaces = range(len(str(longest_number)) - len(str(current_number)))
    return number_of_spaces


for number in range(1, num_of_numbers + 1):
    for space in calculate_spaces(num_of_numbers, number):  # adds spaces to make the digits in line
        print(" ", end='')
    print(f"{number} ^ {exponent} = {number ** exponent}")
