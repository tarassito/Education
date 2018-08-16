# print(f'{__name__}, __file__: {__file__}, __package__: {repr(__package__)}')
# print(f'print from {__name__}')

def func_a():
    print(f'func name: {func_a.__name__} from {__name__}')

def func_b():
    print(f'func name: {func_b.__name__} from {__name__}')