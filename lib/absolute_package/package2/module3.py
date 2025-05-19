# Absolute import (recommended - clear and explicit)
from absolute_package.package1.module1 import function1

def module3_function():
    print("Module 3 is calling:")
    function1()  # Will print "Function 1 in module 1"