def final(a, r, w, v, t):
    BAC = (((a * 10) / (r * w)) * 100 - (v * t))
    return (BAC);


def nosd():
    cnosd = '0'
    a = 0
    while nosd == '0':
        cnosd = int(input())
        if cnosd < 99:
            a = cnosd * 10
            final()
        else:
            nosd()


def hours():
    choiceh = '0'
    t = 0
    while choiceh == '0':
        choiceh = int(input("How many hours has it been since you've drunk?"))
        if choiceh < 25:
            t = choiceh
            nosd()
        else:
            hours()

def weight():
    choicew = '0'
    w = 0
    while choicew == '0':
        choicew = int(input("How much do you weigh in kg?"))
        if choicew < 1000:
            w = choicew * 1000
            hours()
        else:
            weight()





def gender():
    choice = '0'
    r = 0
    while choice == '0':
        choice = input("Are you male or female?")
        if choice == 'm':
            r = 0.68
            weight()
        elif choice == 'male':
            r = 0.68
            weight()
        elif choice == 'f':
            r = 0.55
            weight()
        elif choice == 'female':
            r = 0.55
            weight()
        else:
            print("That is not a valid input")
            print("Please try again")
            gender()




gender()




