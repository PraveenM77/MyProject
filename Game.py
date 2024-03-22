import random
count=0
while count<20:
    comp_choice=random.randint(1,6)
    ur_choice=int(input("Enter your choice"))
    if comp_choice==ur_choice:
        print("You win")
    else:
        print("Computor win")
    count=count+1
