list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number_i = list_numbers.index(max(list_numbers))
last_number_i = list_numbers.index(list_numbers[-1])

list_numbers[max_number_i], list_numbers[last_number_i]  = list_numbers[last_number_i], list_numbers[max_number_i]

print(list_numbers)
