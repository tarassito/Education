import sys
# print(sys.path)  # ['/home/oshto/Education/Ostap/import_examples', '/home/oshto/Envs/education/lib/python3.6/site-packages']

# Absolute import
from package.package_a import module_a
from package.package_b import module_b

# Importing package: if run from terminal (1: looking for __init__.py, 2: load __main__.py if exists)
# python -m package

# importing package in script does nothing
import package


print(f"{list(filter(lambda x: 'package' in x, sys.modules))}")

