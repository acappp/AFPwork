# Function that calculates the BAC
def calcBAC(a, r, w, t):
    # Values must be converted to float for the program to work
    a = float(a)
    r = float(r)
    w = float(w)
    t = float(t)
    BAC = a/(r*w)*100 -(0.00015*t)
    return BAC


# Start of program
# Gathers all required inputs from the user
try: # Try and except blocks are to prevent the user from entering incorrect values and crashing program
    gender = input("Male(m) or Female?(f)")
except ValueError:
    print("you have entered an incorrect value")
    exit(2) # Exit code 2 means the program finished in the input stage
try:
    mass = input("What is your Mass?")
except ValueError:
    print("you have entered an incorrect value")
    exit(2)
try:
    drinks = int(input("How many standard drinks have you consumed?"))
except ValueError:
    print("you have entered an incorrect value")
    exit(2)
try:
    units = input("Kilograms(k) or Pounds(p)")
except ValueError:
    print("you have entered an incorrect value")
    exit(2)
try:
    status = input("What is your status? L, P, FL")
except ValueError:
    print("you have entered an incorrect value")
    exit(2)
try:
    t = input("Hours since you have commenced drinking?")
except ValueError:
    print("you have entered an incorrect value")
    exit(2)

# Converts the mass to Kilos or pounds depending on input
if units == 'k' or units == 'K':
    w = mass * 1000
elif units == "p" or units == 'P':
    w = mass * 453.592
else:
    exit(3) # Program finished in the conversion stage

# Sets the value of R based on the gender inputted
if gender == 'M' or gender == 'm':
    r = 0.68
else:
    r = 0.55

a = drinks * 10

# Calls BAC function and returns the value
BAC = calcBAC(a, r, w, t)

# Prints BAC of user
print('your BAC is', BAC)

# Line of code for L and P platers, determines if license should be cancelled
if status == 'l' or 'p':
    if BAC > 0:
        print('License cancelled, interlock device')
        exit(1) # Exit code one means the program finished correctly
    else:
        print('Safe to drive')
        exit(1)


# Line of code for Full license holders, determines if license should be cancelled
if status == 'FL' or status == 'fl':
    if BAC > 0.07:
        print('License cancelled, interlock device')
        exit(1)
    elif 0.05 < BAC < 0.07:
        print('Fine and 10 demerit points')
        exit(1)
    else:
        print('OK to drive')
        exit(1)
