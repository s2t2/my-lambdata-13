# my_lambdata/my_mod.py

def enlarge(n):
    """
    Param n is a number

    Function will enlarge the number
    """
    return n * 100

if __name__ == "__main__":
    # only invoke the code below
    # if running this file from the command-line
    # (not if importing from another file)

    print(enlarge(7))


    x = int(input("Please choose a number (like 5): "))
    result = enlarge(x)
    print(result)
