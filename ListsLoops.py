words = []
sentence = input('Enter a sentence')
words = sentence.split(' ')
print(words)

points = []
gamePoints = input('Enter the points for each game played, E.G 5,6,7,8')
points = gamePoints.split(',')
print(points)

total = 0
for x in points:
    total += int(x)
    print(total)