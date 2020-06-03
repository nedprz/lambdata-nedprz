# my_lambdata/my_mod.py

def pythag(a , b):
    """
    Params a and b are numbers
    Function will find length of side c of pythagorean triangle
    """
    return (a**2 + b**2)**.5



if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    a = int(input("A: "))
    b= int(input("B: "))
    print(pythag(a,b))




def dist(lat1,long1,lat2,long2):
    """
    Params are longitude and latitude values (floats)

    Function will generate the distance between them (in degrees)
    """
    return ((lat2-lat1)**2 + (long2-long1)**2)**.5



if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    lat1 = float(input("lat1: "))
    long1= float(input("long1: "))
    lat2 = float(input("lat2: "))
    long2 = float(input("long2: "))

    print(dist(lat1,long1,lat2,long2))