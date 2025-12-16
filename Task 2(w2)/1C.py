import math
def is_square():
    test=True
    while test==True:
        n=int(input("Enter a number to test if it is a perfect square: "))
        number=math.sqrt(n)
        floor=math.floor(number)
        if floor*floor==n:
            print(n,"is a perfect square")
        else:
            print(n,"is not a perfect square")
        answer=input("Do you want to do it again? (yes/no) ")
        if answer=="yes":
            test=True
        else:
            test=False
is_square()
   
