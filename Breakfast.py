

breakfast = ['Froot Loops', 'Cocoa Pebbles', 'Honeycomb', 'Wheaties', "Cap'n Crunch"]
def cereal_time():
  for cereal in breakfast:
    if cereal[-1] == "s":
        print (cereal + " are yummy!!")
    else:
        print (cereal + " is yummy!!")
cereal_time()
