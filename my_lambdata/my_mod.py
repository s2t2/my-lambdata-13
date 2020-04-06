# my_lambdata/my_mod.py

def enlarge(n):
    """
    Param n is a number

    Function will enlarge the number
    """
    return n * 100


#x = 5
x = int(input("Please choose a number (like 5): "))
result = enlarge(x)
print(result)
