# create a main function that runs when this file is executed
def main():
    print('Hello user!')
    print('This program will ask you for a temperature')
    print('In Fahrenheit.')
    print('--------------------------------------------')
    val = int(input('Enter a value'))
    ftoc(val)



# Create a funtion to convert fahrenheit to celsius
def ftoc(fah):
    # fah = int(input('Enter a temperature'))
    cel = (fah-32) * 5/9
    print('{0} Fahrenheit = {1:.2f} Celsius'.format(fah, cel))

main()
