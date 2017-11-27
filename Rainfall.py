print("The purpose of this application is to manipulate the monthly rainfall data entered")
rainFall = []
sentence = input("Enter the rainfall data seperated by spaces")
rainFall = sentence.split(' ')
print("This is the data you entered", rainFall)


total = 0
for x in rainFall:
    NRain = len(rainFall)
    total += int(x)
    average = (total / NRain)
print(average)

for i in range(len(rainFall)):
    rainFall[i] = int(rainFall[i])
high = max(rainFall)
low = min(rainFall)

print("The highest entered value was", high)
print("The lowest entered value was", low)