# Stores all the supects as variables
suspect1 = 'GCGGCTGATGCGCAAGACGATAGGCGGGGTTATAGCGCGGCAGCGCGTTCTCCTGAGGTCATCCTGGTCCTACTATACAACCGAGAGGACTGATTGATTGACAA' \
           'CGCTGCGATTACACAGACGGAGCATAACTGTGTATCTCCTATGGCCCCTTCACATAGACAACGGAGCCCGAGTATGGACGCGCAGGTTAACACCTGGCTCCAGA' \
           'ATACTTCACTAGATACCTTCGCCGGGACTGTGCGTGCCAAGA'
suspect2 = 'GCAGCCGAACCGTGATCTTAAGTAAGAATTGCACTGGCGTCTTGGTTAGACATCGAAGTAGCATGCATTATGCTTCGTCTGTGTAGCCGATCCTCGTCCACCCC' \
           'GCACCCAGCATGGCATCACCTACTTTTTGCGGGAATGTCTACTCCGAATACTTGACCTTGGGGTATAGGTTGCGAGCATAACGAGTAGGCGGACTCCCAAATTT' \
           'AGGCGTAAAGAACCCGGTACGTCCTTGCTTCCCAATTTGAAT'
suspect3 = 'CCGACTCCCCATTGCCCTTTGCGAGAGACGACTTATACTAATCTTTTGGACAAAGCTAAGCCTGCCAAGTGGGGCAGAAGGTTTCCTCAGGGGTCCACATAGAC' \
           'CACCATTACAAGTCAGTAGGGCTGATTTCGAACTTGATCAGAACGACCTTTTAGGTGCCGTCGTCTATAGCTCCACTATATATTCGGGAATAGGGCATTACTTT' \
           'CATCCACCATTTGCAACCAGAGACTAAGCGTCTGCCAGTGAC'
suspect4 = 'GACCTATGCCTACTTTGGCTGTCGTGTTATAGAGTGAGAAACGCGCATACGTCCTACAATGGGCCTCGTAGGGTATACATCCCATTTAAGGTCGAGACTAGAAG' \
           'AATTGCCGCGGTCTTCTGGATAAACACTCTGCGTCTTCTACCACATGTAAACCACGGCCCTTCCGTTTATGTAGAGCTACCCGGTTCAGGGTATCGTAACACAT' \
           'TTTTTCAACCAAGTGGTAACTCACAGAACAAAACGACTTTCC'
suspect5 = 'ATTACTGCTGAGGGTGCCGCATTATATAGCTTCGAATGCTGGGCCTGGCCGCGTGCCTTATGTAGAGAGGGCAACGAACGCCGTCCCGAGCAACTATAGGTTTT' \
           'GGCCAAGCGTACGGACTAAGAAGGGCTGTGCTCGTTGGGTTCGCGCGGTCACCATAGTCTGGTTATAGATCGGTTTACAAGCCAATCAATGAAGTTATAAAATG' \
           'CTGCTTTCGTCACATGGGTCGTTCCAACTATGCCTCCGTACG'

# Stores all fragments as Variables
f1 = 'TGAC'
f2 = 'ACCG'
f3 = 'GGCTG'
f4 = 'CTATG'
f5 = 'ATTGCC'
f6 = 'GCATTA'

# Function that starts the program, gives basic information and then leads to the main parts
def opening():
    print("This Program is designed to locate a specific sequence in several sets")
    print("of DNA, Specifically used for finding the suspects of a crime.")
    print("                           Version 1.2")
    print("---------------------------------------------------------------")
    main()

# main process, lets the user pick the suspect
def main():
    choice = '0'
    while choice == '0':
        choice = int(input("Please choose the suspect you would like to analise (1, 2, 3, 4 or 5)"))
        # There is a specific function for each suspect, choosing here leads to eah of them
        if choice == 1:
            sus1()
        if choice == 2:
            sus2()
        if choice == 3:
            sus3()
        if choice == 4:
            sus4()
        if choice == 5:
            sus5()
        else:
            print("That is not a valid input")
            print("Please try again")
            main()

# These find each fragment in the supect and outputs an idex number for each to tell the user where they are
def sus1():
    sus = suspect1
    a = sus.find(f1)
    print("Fragment 1 is at index number", a)
    b = sus.find(f2)
    print("Fragment 2 is at index number", b)
    c = sus.find(f3)
    print("Fragment 3 is at index number", c)
    d = sus.find(f4)
    print("Fragment 4 is at index number", d)
    e = sus.find(f5)
    print("Fragment 5 is at index number", e)
    f = sus.find(f6)
    print("Fragment 6 is at index number", f)
    exit()

def sus2():
    sus = suspect2
    a = sus.find(f1)
    print("Fragment 1 is at index number", a)
    b = sus.find(f2)
    print("Fragment 2 is at index number", b)
    c = sus.find(f3)
    print("Fragment 3 is at index number", c)
    d = sus.find(f4)
    print("Fragment 4 is at index number", d)
    e = sus.find(f5)
    print("Fragment 5 is at index number", e)
    f = sus.find(f6)
    print("Fragment 6 is at index number", f)
    exit()

def sus3():
    sus = suspect3
    a = sus.find(f1)
    print("Fragment 1 is at index number", a)
    b = sus.find(f2)
    print("Fragment 2 is at index number", b)
    c = sus.find(f3)
    print("Fragment 3 is at index number", c)
    d = sus.find(f4)
    print("Fragment 4 is at index number", d)
    e = sus.find(f5)
    print("Fragment 5 is at index number", e)
    f = sus.find(f6)
    print("Fragment 6 is at index number", f)
    exit()

def sus4():
    sus = suspect4
    a = sus.find(f1)
    print("Fragment 1 is at index number", a)
    b = sus.find(f2)
    print("Fragment 2 is at index number", b)
    c = sus.find(f3)
    print("Fragment 3 is at index number", c)
    d = sus.find(f4)
    print("Fragment 4 is at index number", d)
    e = sus.find(f5)
    print("Fragment 5 is at index number", e)
    f = sus.find(f6)
    print("Fragment 6 is at index number", f)
    exit()

def sus5():
    sus = suspect5
    a = sus.find(f1)
    print("Fragment 1 is at index number", a)
    b = sus.find(f2)
    print("Fragment 2 is at index number", b)
    c = sus.find(f3)
    print("Fragment 3 is at index number", c)
    d = sus.find(f4)
    print("Fragment 4 is at index number", d)
    e = sus.find(f5)
    print("Fragment 5 is at index number", e)
    f = sus.find(f6)
    print("Fragment 6 is at index number", f)
    exit()

opening()
