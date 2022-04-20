#!/usr/bin/env python3

print("Are you a welder? Let's find out!")
answer1 = input("Do you know what welding is?\n")

if answer1.capitalize() == "Yes":
    print("I'm sorry")
    answera = input("Do you Weld to make money?\n")
    if answera.capitalize() == "Yes":
        answera1 = input("Is it for food, booze, or meth?\n")
        if answera1.capitalize() == "Food":
            print("You're a welder but your welds look like birdshit.")
        elif answera1.capitalize() == "Booze":
            print("Under .08 and you're in the gate! You're a welder!")
        elif answera1.capitalize() == "Meth":
            print("Meth?! You're definitely a laborer")
        else:
            print("Food, Booze, or Meth. C'mon this isn't that hard..maybe you are a welder.")
    elif answera.capitalize() == "No":
         print("You're probably not that good at it, or have self respect. Congratulations either way, NOT A WELDER!")
    else:
        print("I don't know what you typed, it was probably stupid, because you're a welder.")

elif answer1.capitalize() == "No":
    print("Welding is the process of joining together metal by heating the surfaces to the point of melting using a blowtorch, electrical arc, or other means and uniting them.")
    answer2 = input("Would you like to know more?\n")
    if answer2.capitalize() == "Yes":
        print("Too bad I'm just trying to hit my 40 lines.")
    elif answer2.capitalize() == "No":
        print("Too bad I'm just trying to hit my 40 lines.")
    else:
        print("Too bad I'm just trying to hit my 40 lines.")
else:
    print("Yes or No answers, for this question,but now heres my loop.")
    round = 0
    while True:
        round = round + 1
        print("Do you know who's buried in Grants tomb?")
        answer = input("Take a stab at it! --> ")
        if answer.capitalize() == "Grant":
            print("Correct! You must not be a welder!")
            break
        elif round == 3:
            print("Yeah, incorrect. You must be a welder. Grant is buried in Grants Tomb!")
            break
        else:
            print("Wrong.. seems like you might be a welder..")

