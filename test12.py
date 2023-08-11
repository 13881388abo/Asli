import random
print("rock", "scissor" ,"paper")

lst = ["rock" , "scissor" , "paper"]

a=input()
b = random.choice(lst)

print("player 1 got==" , a)
print("player 2 got==" , b)

if a == "rock" and b == "scissor":
    print("player 1 won")
elif a == "rock" and b == "paper":
    print("player 2 won")
elif a == "scissor" and b == "paper":
    print("player 1 won")
elif a == "scissor" and b == "rock":
    print("player 2 won")
elif a == "paper" and b == "rock":
    print("player 1 won")
elif a == "paper" and b == "scissor":
    print("player 2 won")
elif a==b:
    print("equaled")