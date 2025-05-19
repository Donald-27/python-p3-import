# Import multiple functions if needed (though module1 only has function1 now)
from absolute_package.package1.module1 import (
    function1,
    
)

def module5_function():
    print("Module 5 is calling:")
    function1()