words = input('Please input a sentence: ').split()
camel_case = ''

first = True
for word in words:
    if first:
        camel_case += word.lower()
        first = False
    else:
        if len(word) < 2:
            camel_case += word
        else:
            camel_case += word[0:1].upper()
            camel_case += word[1:len(word)].lower()

camel_case.replace('.', '')
camel_case.replace('#', '')
camel_case.replace('/', '')
camel_case.replace('\\', '')

print('This is your sentence as a filename in camel case:')
print(camel_case)
