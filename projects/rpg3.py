#!/usr/bin/env python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Fannypack : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  if "item2" in rooms[currentRoom]:
    print('You also see a ' + rooms[currentRoom]['item2'])
  if "item3" in rooms[currentRoom]:
      print('and a ' + rooms[currentRoom]['item3'])
  if "item4" in rooms[currentRoom]:
      print('and a ' + rooms[currentRoom]['item4'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item' : 'Covid-Mask',
                  'north' : 'Basement',
                  'west' : 'Upstairs Hall',
                  'item2' : 'Buschs Baked Beans'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'east' : 'Garage',
                  'west' : 'Upstairs Hall',
                  'item' : 'Angry Red-Headed Python Instructor'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south' : 'Garage',
                  'item' : 'Vaccine Papers',
                  'north' : 'Pantry'
               },
            'Garage' : {
                  'north' : 'Dining Room',
                  'west' : 'Kitchen',
                  'item' : 'pile of dead babies',
                  'item' : 'red ferrari'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie'
              },
            'Basement' : {
                  'south' : 'Hall',
                  'item' : 'whip and chains'
                   },
            'Upstairs Hall' : {
                  'south' : 'Playroom',
                  'north' : 'Bedroom',
                  'west' : 'Bathroom',
                  'east' : 'Hall',
                  'item' : 'whip and chains'
                  },
            'Bedroom' : {
                  'east' : 'Attic',
                  'south' : 'Upstairs Hall',
                  'west' : 'Bathroom'
                  },
            'Bathroom' : {
                  'east' : 'Upstairs Hall',
                  'west' : 'Bedroom',
                  'south' : 'Closet',
                  'item' : 'BIG BLACK DILDO =======D---'
                  },
            'Closet' : {
                  'north' : 'Bathroom',
                  'item' : 'cucumber',
                  'item' : 'tube of vaseline'
                  },
            'Playroom' : {
                    'north' : 'Upstairs Hall',
                    'east' : 'Attic',
                    'item' : 'glitter',
                    'item' : 'bodyoil',
                    'item' : 'LIVE: hamster',
                    'item' : 'plastic tube'
                    },
            'Attic' : {
                    'west' : 'Upstairs Hall',
                    'item' : 'dead thai lady boy'
            }
         }

#start the player in the Hall
currentRoom = 'Attic'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get':
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get

  if "item2" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item2']:
      inventory += [move[1]]
      print(move[1] + ' got!')
      del rooms[currentRoom]['item']
  else:
      #tell them they can't get it
        print('Can\'t get ' + move[1] + '!')

  if move[0] == 'take':
     #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
         #add the item to their inventory
       inventory += [move[1]]
       #display a helpful message
       print(move[1] + ' got!')
       #delete the item from the room
    del rooms[currentRoom]['item']
     #otherwise, if the item isn't there to get
    #else:
       #tell them they can't get it
       #print('Can\'t take ' + move[1] + '!')

  ## Define how a player can win
  if currentRoom == 'Garage' and 'Covid-Mask' in inventory and 'Vaccine Papers' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  if currentRoom == 'Basement' and 'whip and chains' in inventory:
      print('You are a dirty gender neutral pronoun')

  if currentRoom == 'Kitchen' and 'whip and chains' not in inventory:
      print('A figure with a rubber phyallic object strapped to its forhead has got you... GAME OVER!')
      break

  if currentRoom == 'Kitchen' and 'whip and chains' in inventory:
      print('\nA monster approaches you and runs away after seeing your whip and chains')
 # ASK CHAD FOR HELP TO NOT BREAK GAME - MOVING BACK INTO ROOM AFTER FIRST ENTRANCE
  if currentRoom == 'Kitchen' and 'whip and chains' in inventory:
      del rooms[currentRoom]['item':'monster']

  #elif rooms[currentRoom]

  ## If a player enters a room with a monster
  #elif 'item' in rooms : 'Kitchen', and 'monster' in rooms[currentRoom]['whip and chains']:
    #print('A figure with a rubber phyallic object strapped to its forhead has got you... GAME OVER!')
