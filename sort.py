def sort(width, height, length, mass):
    #Calculate the volume of the pkg
    volume = width * height * length
    
    #determine if the pkg is bulky
    is_bulky = volume >= 1000000 or width>= 150 or height >= 150 or length >= 150
    
    #determine if the pkg is heavy
    is_heavy = mass >=20
    
    # If the package is both bulky and heavy, it is rejected
    if is_bulky and is_heavy:
        return "REJECTED"
    # If the package is either bulky or heavy (but not both), it is special
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
    
    
if __name__ == "__main__":
    print(sort(200, 100, 100, 25))  #"REJECTED"
    print(sort(10, 20, 20, 5))      #"STANDARD"
    print(sort(20, 30, 60, 30))     #"SPECIAL"
