# print(f'{__name__}, __file__: {__file__}, __package__: {repr(__package__)}')
# print(f'print from {__name__}')

__all__ = ['func_c']

def func_c():
    print(f'func name: {func_c.__name__} from {__name__}')
