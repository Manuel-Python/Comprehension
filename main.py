import random

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

in_names = [name for name in names if "dd" in name]
print(in_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_nums = [n * n for n in numbers]
print(squared_nums)

even_nums = [n for n in numbers if n % 2 == 0]
print(even_nums)

print("*" * 80)

nums1 = []
nums2 = []

with open('file1.txt') as f:
    list1 = f.readlines()
    for line in list1:
        num = int(line.strip())
        nums1.append(num)

print(nums1)

with open('file2.txt') as f:
    list2 = f.readlines()
    for line in list2:
        num = int(line.strip())
        nums2.append(num)

print(nums2)

dif_nums = [n for n in nums1 if n in nums2]

print(dif_nums)

product_nums = [n * n for n in nums1 if n in nums2]
print(product_nums)

print("*" * 80)

# new_dict =  {new_key:new_value for item in list}
# new_dict = { new_key:new_value for (key,value) in dict.items()}

names1 = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names1}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score > 50}
print(passed_students)
