def NULL_not_found(object: any) -> int:
    
    x = type(object)
   
    if x is type(None):
        print(f"Nothing: {object} {x}")
    else:
        print (x)
        print(object)
        return 1       

    return 0

""" https://realpython.com/null-in-python/
