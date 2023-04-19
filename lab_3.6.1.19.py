my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

new_list = []

for element in my_list:
    if element in new_list:
        continue
    else:
        new_list.append(element)

print("The list with unique elements only:")
print(new_list)
