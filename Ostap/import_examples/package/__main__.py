import sys
print(f'{__name__}, __file__: {__file__}, __package__: {repr(__package__)}')
print(f'Imported package from {__name__}')
print(f"{list(filter(lambda x: 'package' in x, sys.modules))}")
