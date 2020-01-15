words = input('Please input a sentence: ').split()
first_word = str(words[0].lower)
rest_of_words = words[1:]
rest_of_words_capitalized = [word[0:1].upper() + word[1:len(word)].lower() for word in rest_of_words]
camel_case = first_word

for word in rest_of_words_capitalized:
    camel_case += word

# Removing symbols we don't want
camel_case = camel_case.replace('.', '')
camel_case = camel_case.replace('#', '')
camel_case = camel_case.replace('/', '')
camel_case = camel_case.replace('\\', '')

print('This is your sentence as a filename in camel case:')
print(camel_case)
