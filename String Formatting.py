print("Hello World")

name = input('You? ')
age = int(input('age ? '))

#The comma simply outputs the result
print('Hello ', name, age)

#The + tries to construct a string to display and it will only work with unt if they are converted to string first
print('Hello ' + name + str(age))

print('Hello {0} you are {1} years old'.format(name, age))