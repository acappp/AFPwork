def main():
    print('Hello user!')
    print('This Program will convert Australian dollars To Japanese yen')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    menu()

def AusJpn(aus):
    jpn = (aus) * 84.97
    print('{0} AUS Dollar(s) = {1:.2f} JPN Yen'.format(aus, jpn))
def JpnAus(jpn):
    aus = (jpn) / 84.97
    print('{0} JPN Yen = {1:.2f} AUS Dollar(s)'.format(jpn, aus))

def menu():
    choice = '0'
    while choice == '0':
        print('')
        print('1. Converts AUS to JPN')
        print('2. Converts JPN to AUS')
        print('3. End Program')
        print('')
        choice = input("Please make a choice: ")
        if choice == "3":
            print("Program has ended")
            break
        if choice == "2":
            val = float(input('Enter a value ¥'))
            JpnAus(val)
            menu()
        if choice == "1":
            val = float(input('Enter a value $'))
            AusJpn(val)
            menu()
        else:
            print("Not a valid input, please try again")
            menu()

main()