def is_year_leap(year):
    return year % 4 == 0


my_year = int(input("Введите год: "))
result = is_year_leap(my_year)
print(f"год {my_year}: {result}")
