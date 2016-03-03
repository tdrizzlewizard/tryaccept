number = raw_input("Give number:")
finalnumber = "Tom"

while finalnumber == "Tom":
    try:
        finalnumber = int(number)
        
       

    except ValueError:
        print("Thats not a number")
        number = raw_input("New Guess:")
        
print("Double that is {}.".format(finalnumber * 2))