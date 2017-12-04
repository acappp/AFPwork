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

def opening():
    print("This Program is designed to locate a specific sequence in several sets")
    print("of DNA, Specifically used for finding the suspects of a crime.")
    print("                           Version 0.1")
    print("---------------------------------------------------------------")
    main()

# def process():



def main():
    choice = '0'
    while choice == '0':
        choice = input("Please choose the suspect you would like to analyise ")
        if choice == 'suspect 1' or 'suspect1':
            sus = suspect1
            #process()
        if choice == 'suspect 2' or 'suspect2':
            sus = suspect2
            #process()
        if choice == 'suspect 3' or 'suspect3':
            sus = suspect3
            #process()
        if choice == 'suspect 4' or 'suspect4':
            sus = suspect4
            #process()
        if choice == 'suspect 5' or 'suspect5':
            sus = suspect5
            #process()
        if choice != 'suspect 1' or 'suspect1' or 'suspect 2' or 'suspect2' or 'suspect 3' or 'suspect3' or 'suspect 4' or 'suspect4' or 'suspect 5' or 'suspect5':
            print("That is not a valid input")
            print("Please try again")
            main()

f1 = 'TGAC'
f2 = 'ACCG'
f3 = 'GGCTG'
f4 = 'CTATG'
f5 = 'ATTGCC'
f6 = 'GCATTA'


opening()
