temperature = int(input('Whats the room temperature? '))
# temperature = 90
while temperature > 75:
  print ("The Temperature is " + str(temperature) + ", crank the AC!")
  temperature -= 3
  if temperature <= 75:
      print ("75. Ahh, that's better.")
