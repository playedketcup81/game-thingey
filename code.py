q1 = input("do you like fps? y or n")
ya = ("y")
na = ("n")

if q1 == ya:
    q1a1 = input("do you like modern games(y) or sci fi(n)")
    if q1a1 == na:
        print("then i think you'll like halo or half life or if you like movement shooters then titanfall 2 ")
        exit()
    else:
        print("i think you might like call of duty or counter strike")
        exit()

else:
    q2 = input("do you like rpgs? y or n")

if q2 == ya:
    q2a1 = input("do you like open world(y) or like mmo types(n)")
    if q2a1 == ya:
        print("i think you might like skyrim or fallout new veges or if your up for the chalige  dark souls")
    else:
        print(" then i think you might like WoW or diablo")
else:
    q3 = input("do you like open world games y or n ")

if q3 == ya:
    q1a1 = input("do you like games were your tasked to survive(y) or you can walk around a city(n)")
    if q1a1 == ya:
        print("i think you might like minecraft or subnatica")
    else:
        q1a2 = input("do you like old games or moden games?")
        if q1a2 == ya:
            print(" i think you might like red dead redemption or assassin creed")
        else:
            print("i think you might like gta or wach dogs")
else:
    q4 = input(" do you like top down games")

if q4 == ya:
    q4a1 = input("do you like survie(y) games or games where you conqore things(n)")
    if q4a1 == ya:
        print(" i think you might like rim world")
    else:
        print("i think you might like age of empiers or command and conquer")
else:
    q5 = input("do you like simulators")


if  q5 == ya:
    q5a1 = input("do you like simulators where you have a fp point of view(y) or do you want more options(n) ")
    if q5a1 == ya:
        q5a2 = input("do you like to hunt(y) or to drive(n)")
        if q5a2 == ya:
            print("i think you might like call of the wild ")
        else:
            print("i think you might like beamng drive or truck driving sim ")
else:
    q5a3 = input("do you like battle sims(y) or do you like to have control over somthing(n)")
    if q5a3 == ya:
        print("i think you might like tabs")
    else:
        print("i think you might like the sims")
