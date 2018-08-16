print('This module runs when the package executes with -m flag')

# python -m package_b  # This module runs when the package executes with -m flag

# when package dont have __main__.py
# python -m package_a  # No module named package_a.__main__; 'package_a' is a package and cannot be directly executed