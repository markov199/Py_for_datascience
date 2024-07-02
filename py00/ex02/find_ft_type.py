
def all_thing_is_obj(object: any) -> int:
    
    x = type(object)

    if x is list:
        print(f"List :  {x}")
    elif (x == tuple):
        print(f"Tuple :  {x}")
    elif (x == set):
        print(f"Set :  {x}")
    elif (x == dict):
        print(f"Dict :  {x}")
    elif (x == str):
        print(f"{object} is in the kitchen :  {x}")
    else:
        print(f"Type not found {x}")
        

    return 42