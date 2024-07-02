def ft_filter(func, list) -> list:
    if func is None:
        return (i for i in list if i)
    else :
        return(i for i in list if func(i))

"""
print(filter.__doc__)

filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.

"""