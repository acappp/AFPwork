#this is the sequence to count

#mySequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

mySequence = input("Please enter the sequence you would like to use")

total = len(mySequence)
#Count the number of C and G in sequence
numC = mySequence.count('C')
print(numC)
numG = mySequence.count('G')
print(numG)

#works out the percentage of C and G
perC = ((numC/total)*100)
perG = ((numG/total)*100)

#Adds C and G together
content = (perC + perG)

# Round, rounds the number to 2 decimal places.
#places, I can easily add more placeholders and variables
print('The GC content of the sequence is {0:.1f}%'.format(content))
print(round(content, 2))