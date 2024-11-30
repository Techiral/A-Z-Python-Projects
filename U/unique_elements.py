# This function takes a list as input and returns a new list with unique elements.
def unique_elements(input_list):
    unique = []
    for i in input_list:
        if i not in unique:
            unique.append(i)
    return unique
l = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(l)
print(result)
