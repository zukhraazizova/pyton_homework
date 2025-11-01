def is_leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


print(2024, is_leap_year(2024))  # True
print(2023, is_leap_year(2023))  # False
