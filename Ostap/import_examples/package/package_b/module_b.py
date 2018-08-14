# Relative explicit import
from ..package_a import module_d #  two dots means upper level directory
from . import module_c # one dot means current(of this file) directory

# Relative implicit import
# import module_c
# in python2 will look at current file directory first, then look at sys.path(pythonpath, site-packages, etc)

# Implicit relative imports should never be used and have been removed in Python 3.
# Changed in version 3.3: The import system has been updated to fully implement the second phase of PEP 302.
# There is no longer any implicit import machinery.
