# new_list = [new_item for item in list] 
# we can do list comprehension on number of list or string or on any range

# on list
number = [1, 2, 3]
new_number = [n+1 for n in number]

# on range
new_range = [n * 2 for n in range(1, 5)]
print(new_range)

# conditional list comprehension: new_list = [new_item for item in list if test]
name_list = ["ladu", "lili", "mina", "ladubai"]

new_name = [name for name in name_list if len(name) < 5]
print(new_name)

all_cap_list = [name.upper() for name in name_list if len(name) > 4]
print(all_cap_list)
