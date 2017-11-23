str_asd = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print("Entered value", str_asd)
print("")

#Replaces all values with their compliments
#Lower case letters so that they are not replaced twice
str_asd = str.replace(str_asd, 'A', 'c')
str_asd = str.replace(str_asd, 'C', 'a')
str_asd = str.replace(str_asd, 'G', 't')
str_asd = str.replace(str_asd, 'T', 'g')
print(str_asd)
print("")

#Replaces lowercase letters with upper case
str_asd = str.replace(str_asd, 'c', 'C')
str_asd = str.replace(str_asd, 'a', 'A')
str_asd = str.replace(str_asd, 't', 'T')
str_asd = str.replace(str_asd, 'g', 'G')
print("The Compliment is:")
print(str_asd)