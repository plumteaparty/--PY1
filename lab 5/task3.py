def get_unique_list_numbers() -> list[int]:
    import random
    rand = [random.randint(-10, 10)]
    while len(rand) < 15:
        rand_n = random.randint(-10, 10)
        if rand_n not in rand:
            rand.append(rand_n)
    return rand


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
