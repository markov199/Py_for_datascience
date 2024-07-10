def NULL_not_found(object: any) -> int:
    
    x = type(object)
   
    if x is type(None):
        print(f"Nothing: {object} {x}")
    elif x is float:
        if object != object:
            print(f"Cheese: {object} {x}")
    elif x is int and object is 0:
            print(f"Zero: {object} {x}")
    elif x is str and object is '':
            print(f"Empty: {object} {x}")
    elif x is bool and object is False:
            print(f"Fake: {object} {x}")
    else:
        print("Type not Found")
        return 1       

    return 0
"""
None is a powerful tool used to define a null variable in the Python toolbox.
Like True and False, None is an immutable keyword and None can be used to mark missing values and also default parameters.
Test for None with identity operator (is and is not).

NaN (Not a Number): NaN represents missing or undefined data in Python. It is typically encountered while performing mathematical operations that result in an undefined or nonsensical value. NaN is a floating-point value represented by the float('nan') object in Python.

Zero: Zero (0) is a numerical value that represents a valid number indicating nothing or the absence of quantity. It is not the same as NaN, as NaN represents a specific numeric value.

Empty: Empty values refer to variables or objects that have not been assigned any value. They differ from NaN and zero, as they represent the absence of any value or data.

ref
 https://realpython.com/null-in-python/
 
"""
