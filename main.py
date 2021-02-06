numbers = [1, 2, 3]
# new_numbers = [new_item for item in list]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Manuel"
letters_list = [letter for letter in name]
print(letters_list)

double_nums = [n + n for n in range(1, 5)]
print(double_nums)

# new_numbers = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 4]
print(short_names)
print(long_names)
