first_list = ["FirstItem", "FriendsList", "MyTuple"]
modified_list = []
for variable_name in first_list:
    snake_case = ""
    for number, char in enumerate(variable_name):
        if char.isupper() and number != 0:
            snake_case += "_"
        snake_case += char.lower()
    modified_list.append(snake_case)
print(modified_list)


