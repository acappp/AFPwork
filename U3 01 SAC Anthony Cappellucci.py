# This function recieves imperial measurement of the height and returns it as a metric equivalent
def convertHeight(height):
    height = float(height)
    # Values must be converted to float
    h = height * 0.3048
    return h

# This function recieves imperial measurement of the Weight and returns it as a metric equivalent
def convertWeight(weight):
    # Values must be converted to float
    weight = float(weight)
    w = weight * 0.45359237
    return w

# This function decides if the user is Underweight, Healthy, overweight or obese depending on BMI
def getBMIcategory(bmi):
    if bmi <= 18.5:
        category = 'Underweight'
        return category
    # Returns the appropriate category to the equation
    elif bmi >= 18.5 <= 25:
        category = 'Healthy weight'
        return category
    elif bmi >= 25 <= 30:
        category = 'Overweight'
        return category
    elif bmi == 30 >= 30:
        category = "Obese"
        return category

# Takes input from the user and assigns a variable for each
# Try and except Value eroor are in place to prevent the program from crashing
try:
    units = input('Would you like to use Metric(m) or Imperial(I)?')
except ValueError:
    print("you have entered an incorrect value")
    exit(2)
try:
    height = int(input('Please input your height (in feet/metres)'))
except ValueError:
    print("you have entered an incorrect value")
    exit(2)
try:
    weight = int(input('Please enter your weight (in lbs/kilograms)'))
except ValueError:
    print("you have entered an incorrect value")
    exit(2)

# If the user selects imperial it will run the conversion function above
if units == 'i' or units == 'I':
    h = convertHeight(height)
    heightInMetres = h
    w = convertWeight(weight)
    weightInKgs = w
elif units == 'm' or units == 'M':
    # If the user chooses metric the values will remain the same
    heightInMetres = height
    weightInKgs = weight
else:
    print("you have entered an incorrect value")
    exit(2)

# The BMI determining equation weight / height to the power of 2
bmi = weightInKgs / (heightInMetres * heightInMetres)

# Calls the category function
category = getBMIcategory(bmi)
# Prints the users BMI and Category
print("Your Bmi is", bmi)
print('you are obese', category)
exit(1)
# Exit code 1: the program finished successfully
# Exit code 2: the program ended because of an incorrect value