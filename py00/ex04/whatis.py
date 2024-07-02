import sys

try:
    y = len(sys.argv)
    if y == 1:
        exit(1)
    assert y == 2, "more than one argument is provided"
    try:
        number = int (sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    if number % 2 == 0:
        print("I'm Even")
    else:
        print("I'm odd")
except AssertionError as msg:
    print("AssertionError:", msg)