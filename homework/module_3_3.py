#1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(22, 'STRING', False)
print_params('arg1', 'arg2')
print_params(b = 'Urban')
print_params(b = 25)
print_params(c = [1, 2, 3])

# 2
values_list = [123, 'password', True]
values_dict = {'a': 321, 'b': 'login', 'c': False}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [54.32, 'value1']
print_params(*values_list_2, 42)