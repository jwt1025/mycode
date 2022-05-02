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


    while question not in ["last","last2","last3"]:
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

def pizza():
    pizza= {
            1:{"q":"Right off the bat, does pineapple belong on pizza?",
                "yes":"last" ,
                "no": 2},
            2:{"q":"Are you a vegetarian?",
               "yes": "last2",
               "no": 3},
            3:{"q": "Are you from Chicago?",
               "yes": "last3",
               "no": "last4"}
            }
    os.system("clear")
    question = 1

    while question not in ["last","last2","last3","last4"]:
        print(pizza[question]["q"])

        answer= input("\n").strip().lower()

        os.system("clear")

        if answer in pizza[question]:
            question= pizza[question][answer]

            if question == "last":
                print("Call up your local pizza joint, you're getting a hawaiian pizza!")

            elif question == "last2":
                print("You're ordering a spinach and olive pizza!")

            elif question == "last3":
                print("Lou Malnatis! Hands down, should have been your first choice anayway.")

            elif question == "last4":
                print("Call up Dominoes and get a regular cheese pizza!")



def menu():
    os.system("clear")
    path= input("Does a burger sound good?\n")

    if path.lower().strip() == "yes":
        os.system("clear")
        burger()

    elif path.lower().strip() == "no":
        os.system("clear")
        pizzainput= input("Does a pizza sound better?\n")
        if pizzainput.lower().strip() == "yes":
            pizza()

def startmenu():
    while True:
        os.system("clear")
        initial= input("Are you hungry?\n")

        if initial.lower().strip() == "yes":
            menu()
            break

        elif initial.lower().strip() == "no":
            print("Run again when you can't decide your next meal.")
            break

        else:
            print("Don't be indecisive, that's why you're here! Yes or No.")
            time.sleep(3)
startmenu()
