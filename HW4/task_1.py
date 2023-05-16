str_data = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
str_data = str_data.strip()
pairs = str_data.split('&')
result_dict = {}
for pair in pairs:
    split_pair = pair.split('=')
    if len(split_pair) == 2:
        key, value = split_pair
        if value.isdigit():
            result_dict[key] = int(value)
        else:
            result_dict[key] = value
print(result_dict)
