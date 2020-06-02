# my_lambdata/my_mod.py

def pythag(a , b):
    """
    Param n is a number
    Function will enlarge the number
    """
    return (a**2 + b**2)**.5

# this code breaks our ability to import enlarge from other files, if left in the global scope:
#
# print("HELLO")
# y = int(input("Please choose a number"))
# print(y, enlarge(y))

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    a = int(input("A: "))
    b= int(input("B: "))
    print(pythag(a,b))