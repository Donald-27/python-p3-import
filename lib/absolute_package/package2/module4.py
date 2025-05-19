# Alternative absolute import style
import absolute_package.package1.module1 as p1m1

def module4_function():
    print("Module 4 is calling:")
    p1m1.function1()  # Will print "Function 1 in module 1"