# **kwargs in python

#  called as keyword arguments

#  type of **kwargs is dictionary where as type of *args is tuple


from pandas import value_counts


# def calculate(**kwargs):
#     print(kwargs)
#     for (key, value) in kwargs.items():
#         print(f"key = {key} value = {value}")

#     print(kwargs["add"])
#     print(kwargs["multiply"])


def calculate(n, **kwargs):
    print(kwargs)
    for (key, value) in kwargs.items():
        print(f"key = {key} value = {value}")

    print(kwargs["add"])
    print(kwargs["multiply"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add = 3, multiply = 4)