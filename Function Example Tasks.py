

def largest_number(list):
    large_number = 0
    for i in list:
        if i > large_number:
            large_number = i

    return large_number

def reverse(revlist):
    rlist = []
    for i in revlist:
        rlist.insert(0, i)

        return rlist



list = []
UI = "\n"
loop = True
while UI != "":
    UI = int(input("Enter a value for the list: "))
    if UI != "":
        list.append(UI)
        print("The current values are: ")
        print(list)
        l = largest_number(list)
        print("Largest number is", l)
        print("")
if(loop):
    valueToPrint = largest_number(list)
    print("Largest value: ", valueToPrint)

listToPrint = ReverseListWhile(list)
print("Reversed list: ", listToPrint)