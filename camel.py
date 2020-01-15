words = input('Please input a sentence: ').split()
camel_case = ''

first = True
for word in words:
    # We don't want the first word capitalized, so making the whole word lower case.
    if first:
        camel_case += word.lower()
        first = False
    # Then we're making the first letter capitalized, and the rest lower.
    else:
        # If it's only one letter or character still remaining, it can just be capitalized.
        if len(word) < 2:
            camel_case += word.upper()
        # If it's more than one, we want to substring the first letter as capitalized, and lowercase the rest.
        else:
            camel_case += word[0:1].upper()
            camel_case += word[1:len(word)].lower()

# Removing symbols we don't want
camel_case = camel_case.replace('.', '')
camel_case = camel_case.replace('#', '')
camel_case = camel_case.replace('/', '')
camel_case = camel_case.replace('\\', '')

print('This is your sentence as a filename in camel case:')
print(camel_case)
