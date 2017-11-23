str1 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
str2 = "AATTC"

#Finds aattc, in the data set
l = str1.find(str2)

#Counts the number of letters in string 1
p = len(str1)

#Subtracts string 1 from string 2
k = (p-l)
print(k)