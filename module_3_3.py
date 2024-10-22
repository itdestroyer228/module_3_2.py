def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25, c = [1,2,3])
values_list = [2, "privet", True]
values_dict = {'a': 'Hello,', 'b': 'Mr.', 'c': 'O'}
print_params(**values_dict)
print_params(*values_list)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
