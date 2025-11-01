def filter_list(lst: list) -> list:
    return [x for x in lst if x % 3 == 0]


lst = [11, 15, 18, 20, 24, 33, 55, 76, 89, 20]
print(filter_list(lst))  # [15, 18, 24, 33]
