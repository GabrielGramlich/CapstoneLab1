count = int(input('How many classes are you taking this semester? '))
counter = 0
classes = []

while (counter < count):    # Only looping once for each class.
    classes.append(input('Enter the name of class #' + str((counter + 1)) + ': '))
    counter += 1

print('The classes you are taking:')
for item in classes:
    print(item)
