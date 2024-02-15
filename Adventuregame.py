import random
#functions
loot = 0
def csystem(ai_name,reward_amount,advancedyesno):
#reward amount is reward gained for win and amount punished for loss
    computer_hp = 5
    player_hp = 5
    loot = 0
    critical_attack = f"{advancedyesno}"      #make this 20% odd
    if critical_attack == "yes":
        critical = 1
        
    #           attack  parry   feint
    options = ["attack","parry","feint"]
    #             0     1         2 


    while True:
        print("You are currently",player_hp,"bar(s)")
        print(f"{ai_name}, is currently",computer_hp,"bar(s)")
        if player_hp <= 0:
            print(f"{ai_name} won")
            loot = loot - reward_amount
            break 

        elif computer_hp <= 0:
            print("you won the battle")
            loot = loot + reward_amount
            break
        print(f"You encountered {ai_name} you will have 3 options to choose from the way you want to fight him you got 4th option to flee")
        player_move = input("Type attack/parry/feint or f to flee(need to have 5 hp bars to flee)").lower()
        if player_move == "f" and player_hp == 5:
            break
        

        if player_move not in options:
            continue

        random_number = random.randint(0,2)

        ai_move = options[random_number]
        print(f"{ai_name} did",ai_move + ".")


        # player win conditions



        if player_move == "attack" and  ai_move =="feint":
            print("you damaged him (1 bar)")
            computer_hp = computer_hp - 1
            critical_chance = random.randint(0,4)   #20%
            if critical_chance == critical:
                computer_hp = computer_hp - 1
                print("Epic you landed critical and damaged enemy with an extra bar")  
            
            
            continue

        elif player_move == "parry" and  ai_move =="feint":
            print("you damaged him (1 bar)")
            computer_hp = computer_hp - 1
            critical_chance = random.randint(0,4)   #20%
            if critical_chance == critical:
                computer_hp = computer_hp - 1
                print("Epic you landed critical and damaged enemy with an extra bar")  
            

            continue

    #rock - attack paper - parry  scissors feint
        elif player_move == "scissors" and  ai_move =="paper":
            print("you damaged him (1 bar)")
            computer_hp = computer_hp - 1
            critical_chance = random.randint(0,4)   #20%
            if critical_chance == critical:
                computer_hp = computer_hp - 1
                print("Epic you landed critical and damaged enemy with an extra bar")  
            

            continue

# from here ai win conditions
        
        elif ai_move == "attack" and  player_move =="feint":
            print(f"{ai_name} damaged you (1 bar)")
            player_hp = player_hp - 1
            critical_chance = random.randint(0,4)   #20%
            if critical_chance == critical:
                player_hp = player_hp - 1
                print(f"Unfortunately {ai_name} landed critical and damaged you with an extra bar")  
            

            




            continue

        elif ai_move == "feint" and  player_move =="parry":
            print(f"{ai_name} damaged you (1 bar)")
            player_hp = player_hp - 1
            critical_chance = random.randint(0,4)   #20%
            if critical_chance == critical:
                player_hp = player_hp - 1
                print(f"Unfortunately {ai_name} landed critical and damaged you with an extra bar")  
            continue

        elif ai_move == "parry" and  player_move =="attack":
            print(f"{ai_name} damaged you (1 bar)")
            player_hp = player_hp - 1
            critical_chance = random.randint(0,4)   #20%
            if critical_chance == critical:
                player_hp = player_hp - 1
                print(f"Unfortunately {ai_name} landed critical and damaged you with an extra bar")  
            continue

        elif player_move == ai_move:
            print("Draw")
            print("parry trade none of hits landed")
            continue

        else:
            print("something went wrong try again")
            continue
        

    print(f"end of battle with {ai_name}")

#beginning basics asking for name

player_name = input("What is your name? lone wanderer")
print("Lets go on an adventure",player_name)
ready = input("Are you ready to go on a new journey!?  yes/no ").lower()
if ready == "yes":
    print("Great")
else:
    quit()


#basic number guessing game from 0 to 10 to determine race simple luck mechanic code rather then writing % system

random_racenum = random.randint(0, 10)
attempts = 0

while True:
    attempts += 1
    player_attempt = input("Race affects luck to determine your race enter number from 0 to 10 (included) less attempts you take to guess randomly generated number better race you'll get ")
    if player_attempt.isdigit():
        player_attempt = int(player_attempt)
        if player_attempt < 0 and player_attempt > 10:
            print("Please enter number between 0 and 10 next time ")
            continue
    else:
        print("Please type number next time response was invalidated")
        continue

    if player_attempt == random_racenum:
        print("You guessed the number ")
        break
    elif player_attempt > random_racenum:
        print("You were above the number")
    elif player_attempt < random_racenum:
        print("you were under the number")


luck = 0

print("You took",attempts,player_name,"to guess the number")
if attempts == 1:
    race = "vesperian"
    luck = luck + 10
elif attempts == 2:
    race = "ganymede"
    luck = luck + 9
elif attempts == 3:
    race = "capra"
    luck = luck+ 8
elif attempts == 4:
    race = "khan"
    luck = luck + 7
elif attempts == 5:
    race = "felinor"
    luck = luck + 6
elif attempts == 6:
    race = "gremor"
    luck = luck + 5
elif attempts == 7:
    race = "canor"
    luck = luck + 4
elif attempts == 8:
    race = "celtor"
    luck = luck+ 3
elif attempts == 9:
    race = "adret"
    luck = luck + 2
else:
    race = "mudskipper"
    luck = luck + 1


print(player_name,"your race is",race,"your luck is",luck)
print("those are your stats.stats will work as resource in this game more you have more things you can do and will have higher chance of success you can gain more luck or exchange it for something use it wisely")
print("from time to time you will get newer info of your stats")



#orgin determination system works same way as race
random_orginnum = random.randint(0, 10)
guesses = 0

while True:
    guesses += 1
    player_guess = input("Enter number between 0 and 10 to determine orgin ")
    if player_guess.isdigit():
        player_guess = int(player_guess)
        if player_guess < 0 and player_guess > 10:
            print("Please enter number between 0 and 10 next time ")
            continue
    else:
        print("Please type number next time response was invalidated")
        continue

    if player_guess == random_orginnum:
        print("You guessed the number ")
        break
    elif player_guess > random_orginnum:
        print("You were above the number")
    elif player_guess < random_orginnum:
        print("you were under the number")




print("You took",guesses,player_name,"to guess the number")
if guesses == 1:
    orgin = "Ministriya"
    luck = luck + 15
elif guesses == 2:
    orgin = "etrea"
    luck = luck + 12
elif guesses == 3:
    orgin = "deepbound"
    luck = luck + 9
elif guesses == 4:
    orgin = "voidheart"
    luck = luck + 7


else:
    orgin = "vigils"
    luck = luck + 3

print("Your orgin is",orgin)
#adventure starts here
while True:
    stats_check = input("You can check your stats anytime by writing (stats)").lower()
    if input() == "stats":
        print(player_name,race,orgin,luck)
    path = input("you have encountered travelling adventurer will you fight him or grind weaker mobs(adventurer/mobs/)").lower()

    if path == "adventurer":
        print("risky decesion",race,player_name)
        fiftypercent = random.randrange(0, 3)  #named variable after risk player took of 50%  
        print("You approached adventurer he has same fighting experience as you what are you going to do cast a spell on him or stab him with a knife")
        player_risk = input("1 for casting a spell 2 for stabbing him with a knife")
        if player_risk == "1":
            print("You won and looted his purse you doubled your luck")
            luck = luck*2
            break
            

        elif player_risk == "2":
            print("you lost and he stole your pouch lost half of your luck")
            luck = luck/2
            break
        else:
            print("Invalid answer you just left adventurer alone after small talk")
            continue
    
    elif path == "mobs":
        print("you have choosen easy path",race,player_name)
        luck = luck + 3  
    
    else:
        print("Invalid answer please try again")
        continue
        


while True:
    player_path2 = input("Where will you grind?(your orgin and race affects decesion you make) (hive/crypt/erisea/depths)").lower()
    if player_path2 == "hive":
        if orgin == "voidheart":
            print("you voidwalked freshie in give gained 30 luck")
            luck = luck + 30
        encounter = input("you encountered pack of threshers in hive what is it you do (flee/fight)")
        if encounter == "flee":
            print("you have escaped the great danger")
            break
        elif encounter == "fight":
            print("you lost your leg to threshers tried sailing away and ended up in depths (-30 luck)")
            luck = luck - 15
        else:
            print("not a valid response")
            continue
    
    if player_path2 == "crypt":
        if orgin == "Ministriya":
            print("you found moonseye tome in crypt(gained 30 luck)")
            luck = luck + 30
        encounter1 = input("2 friends of same guild arrive at crypt what is it you do (flee/talk)").lower()
        if encounter1 == "flee":
            print("you got away safely")
            break
        elif encounter1 == "talk":
            print("they lure you deeper into crypt and grip you at voidzone you fall at depths (-30 luck)")
            luck = luck - 15
        else:
            print("not a valid response try again")
            continue
    if player_path2 == "erisea":
        if orgin == "etrea":
            print("you grinded in peace (gained 30 luck)")
            luck = luck + 30
        encounter2 = input("maxed out trackstar approaches you and asks to test dmg (log/test)").lower()
        if encounter2 == "log":
            print("you got away safely")
            break
        elif encounter2 == "test":
            print("he 1 combos you and corrupted reapers you got sent to depths (-30 luck)")
        else:
            print("not a valid response try again")
            continue
    if player_path2 == "depths":
        print("you got boosted by 3 max pves(gained 30 luck)")
        luck = luck + 30
        encounter3 = input("you encounter a corrupted owl do you risk taking fight (flee/fight)").lower()
        if encounter3 == "flee":
            print("you got away safely")
            break
        elif encounter3 == "fight":
            last_wind = input("dumbass you ended up in fragments of self do you wipe/last_wind").lower()
            if last_wind == "wipe":
                quit()
            elif last_wind == "last_wind":
                continue

csystem("Ganker Abraham Galvigi",25,"yes")
csystem("voidwalker",20,"yes")
csystem("freshie",10,"yes")



if luck > 30 and loot > 0:
    print("Good ending you live a happy and peaceful life")
    if luck > 15:
        print("Netural ending you life an average person's life")
    elif luck < 5:
        print("you spend rest of your time blind")
else:
    print("Trashed ending you life an useless retarded garbage life ")
    
            
   




    









