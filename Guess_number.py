#Guess th number game
import random

rand =random.randint(1,100)
# print(rand)
you = 0
count = 0
while(rand  != you ):

    youno = int(input("Guess The Number Between 1 - 100 : "))
    count+=1
    if(rand < youno):
        print("Guess lower Number...")
    elif(rand > youno):
        print("Guess Greater Number...")
    else:
        print(f"""
              
        Hureyyy!!!!!! YOU WON 
        in {count} attemps..      
            """)

    you = youno
