# T-Rex_Mood = str(input("How are you feeling, O' Awesome T-Rex? Angry, Tired, Bored and/or Hungry?"))
# if T-Rex_Mood = "Angry" and T-Rex_Mood = "Hungry" and T-Rex_Mood = "Bored":
#     print ("How dare you eat the Triceratops???!!!")
# elif T-Rex_Mood = "Tired" and T-Rex_Mood = "Hungry":
#     print ("My Iguanadon!!! You ate my Iguanadon!!!!")
# elif T-Rex_Mood = "Bored" and T-Rex_Mood = "Hungry":
#     print ("Get that little rascal of a Stegasauros! Who does he think he is?!")
# elif T-Rex_Mood = "Tired":
#     print ("Who's a cute little (Um... more like huge.) sleeping T-Rex??!!!")
# elif T-Rex_Mood = "Angry" and T-Rex_Mood = "Bored":
#     print ("Um, Mr. T-Rex... Do you mind killing this Velociraptor thats trying to eat me? Please?")
# elif T-Rex_Mood = "Angry" or T-Rex_Mood = "Bored":
#     print ("Ouch that's loud!! Why'd you roar in my ear??!!!!")
# else:
#     print ("What big,white teeth you have.... You're making me nervous with that grin....")
# This ^ didn't work, not sure why...

angry = True
bored = True
hungry = True
tired = True
if angry and bored and hungry and not tired:
    print ("How dare you eat the Triceratops???!!!")
elif tired and hungry and not angry and not bored:
    print("My Iguanadon!!! You ate my Iguanadon!!!!")
elif hungry and bored and not angry and not tired:
    print("Get that little rascal of a Stegasauros! Who does he think he is?!")
elif tired and not hungry and not bored and not angry:
    print("Who's a cute little (Um... more like huge.) sleeping T-Rex??!!!")
elif angry and bored and not hungry and not tired:
    print("Um, Mr. T-Rex... Do you mind killing this Velociraptor thats trying to eat me? Please?")
# The only way to properly do the or statement here is to make two seperate lines because otherwise
# if all the above conditions are true then python will just print the first of the two it sees which is
# 'Ouch that's loud!! Why'd you roar in my ear??!!!!' and not 'What big, white teeth you have.... You're making me nervous with that grin....'
elif angry and not bored and not angry and not tired:
    print("Ouch that's loud!! Why'd you roar in my ear??!!!!")
elif bored and not angry and not tired and not hungry:
    print("Ouch that's loud!! Why'd you roar in my ear??!!!!")
else:
    print("What big, white teeth you have.... You're making me nervous with that grin....")
# It's interesting that without the "and not"s the above code is dependent on the order of the lines
# If I were to put just tired in the first if statement it will only print
# How dare you eat the Triceratops???!!!
