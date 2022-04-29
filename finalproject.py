#!/usr/bin/env python3

import os
import time





def burger():
    burger= {
        1:{"q":"Do you want a veggie burger?",
            "yes": "last",
            "no": 2},
        2:{"q":"Do you like bacon?",
            "yes": "last2",
            "no":  3},
        3:{"q": "Are you cheap?",
            "yes": "last3",
            "no": "last3"}
            }
        
    os.system("clear")
    question = 1 


    while question != "last" or "last2" or "last3":
        print(burger[question]["q"])


        answer= input("\n").strip().lower()

        os.system("clear")

        if answer in burger[question]:
            question= burger[question][answer]

            if question == "last":
                print("You're going to Burger King, the impossible burger SMACKS!")

            elif question == "last2":
                print("You're heading to Wendy's.. time for a Baconater!")

            elif question == "last3":
                print("Looks like you're going to McDonald's, time for a Big Mac")



def menu():
    os.system("clear")
    path= input("Does a burger sound good?\n")

    if path.lower().strip() == "yes":
        os.system("clear")
        burger()

    elif path.lower().strip() == "no":
        os.system("clear")
        input("Does a pizza sound better?\n")
        if input.lower().strip() == "yes":
            pizza()

def startmenu():
    while True:
        os.system("clear")
        initial= input("Are you hungry?\n")

        if initial.lower().strip() == "yes":
            menu()

        elif initial.lower().strip() == "no":
            print("Run again when you can't decide your next meal.")
            break

        else:
            print("Don't be indecisive, that's why you're here! Yes or No.")
            time.sleep(3)
            startmenu()
startmenu()
