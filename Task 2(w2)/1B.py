import random as rand
def epicness():
 epic=True
 while epic==True:
    names = []
    names2=int(input("How many names do you want to enter? "))
    for i in range(names2):
        names.append(input("names "))
    num_winners=int(input("How many winners do you want to pick? "))
    print("The winners are: ", rand.sample(names,num_winners))
    input("Do you want to do it again? (yes/no) ")
    if input=="yes":
        epic=True
    else:
        epic=False
epicness()


