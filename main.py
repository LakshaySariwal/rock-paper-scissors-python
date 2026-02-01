import random
'''1 for rock
-1 for paper
0 for scissor'''
print("Lets play a game\nchoose anything between \n(r:rock , p:paper and s:scissor)")
computer =random.choice([-1,0,1])
you=input("enter your choice : ")
youdict={"r":1,"p":-1,"s":0}
rdict={1:"rock",-1:"paper",0:"scissor"}
younum=youdict[you.lower()]
print(f"computer chose {rdict[computer]}\n you chose {rdict[younum]}")
if(computer==younum):
    print("draw")
elif(computer==-1 and younum==1):
    print("you lose")
elif(computer==-1 and younum==0):
    print("you win")
elif(computer==1 and younum==0):
    print("you lose")
elif(computer==1 and younum==-1):
    print("you win")
elif(computer==0 and younum==1):
    print("you win")
elif(computer==0 and younum==-1):
    print("you lose")
else:
    print("something went wrong")
