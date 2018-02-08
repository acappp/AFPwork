a = int(input("How many standard drinks have you consumed?: "))
r = input("What gender are you? (M/F): ")
unit = input("Do you use pounds or kilograms?: ")
unit = unit.lower()

w = int(input("What is your mass?: "))
if unit == "kilograms":
  w = w * 1000
elif unit == "pounds":
  w = w * 453.592

licence = input("What license are you currently on?(L/P1/P2/FL): ")
t = int(input("How long since you commenced drinking in hours?: "))
v = int(0.00015)


if r == "M":
  r = 0.68
else:
  r = 0.55


BAC = (((a*10)/(r*w))*100-(v*t))

if licence == "L" or "P":
  if BAC > 0:
    print("License cancelled, interlock device")
  elif licence == "FL":
      if BAC > 0.07:
          print("License cancelled, interlock device")
      elif 0.05 < BAC < 0.07:
          print("Fine and 10 demerit points")
      else:
          print("OK to drive")


print("You have a BAC of",(round(BAC,2)))