Time = int(input("What time is it now? (In military time.)"))
if Time >= 6 and Time < 9:
    print ("Morning is wonderful. Its only drawback is that it comes at an inconvenient time of day.")
elif Time >= 9 and Time <= 16:
    print ("Working hard or hardly working?")
elif Time > 16 and Time <= 20:
    print ("How did it get so late so soon?!")
elif Time > 20 and Time < 22:
    print ("A day without sunshine is like, you know, night.")
elif Time >= 22 and Time< 24 or Time>= 0 and Time< 6:
    print ("Burning the midnight oil!")
else:
     Time = int(input("What time is it now? (In military time.) Try again."))
if Time >= 6 and Time < 9:
    print ("Morning is wonderful. Its only drawback is that it comes at an inconvenient time of day.")
elif Time >= 9 and Time <= 16:
    print ("Working hard or hardly working?")
elif Time > 16 and Time <= 20:
    print ("How did it get so late so soon?!")
elif Time > 20 and Time < 22:
    print ("A day without sunshine is like, you know, night.")
elif Time >= 22 and Time< 24 or Time>= 0 and Time< 6:
    print ("Burning the midnight oil!")     
