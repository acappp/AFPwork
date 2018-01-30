# Keeps all suspects on record, Only one now for simplicity
Suspect = "GCGGCTGATGCGCAAGACGATAGGCGGGGTTATAGCGCGGCAGCGCGTTCTCCTGAGGTCATCCTGGTCCTACTATACAACCGAGAGGACTGATT" \
          "GATTGACAACGCTGCGATTACACAGACGGAGCATAACTGTGTATCTCCTATGGCCCCTTCACATAGACAACGGAGCCCGAGTATGGACGCGCAGG" \
          "TTAACACCTGGCTCCAGAATACTTCACTAGATACCTTCGCCGGGACTGTGCGTGCCAAGA"


# Main program asks the user the fragment they would like to use, then finds that fragment in the suspect
def open():
    choice = int(input("Please choose if you would like to search for Fragment 1, 2, or 3"))
    # The choice determines what 'f' will be set to
    if choice == 1:
        f = "TGAC"
        # This code finds f and sets the number it is located to as a variable.
        a = Suspect.find(f)
        print(a)
    if choice == 2:
        f = "ACCG"
        a = Suspect.find(f)
        print(a)
    if choice == 3:
        f = "GGCTG"
        a = Suspect.find(f)
        print(a)
        # Having this as a function makes it easier to repeat when the wrong answer is inputted by the user
    else:
        open()


# Opens main function
open()