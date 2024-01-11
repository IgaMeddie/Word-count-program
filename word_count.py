book = {}

while True:
    word = input("Enter a word(Enter -999 to quit): ")

    if word == "-999":
        break
    
    elif word in book:
        book[word] += 1

    else: 
        book[word] = 1

if book != {}:
    print("Constructed dictionary: book =", book)
else:
    print("Empty dictionary", book, "\nNothing entered")

for each_word in book:
    print(each_word, book[each_word])

# red
# red
# red
# blue
# green
# blue
# green
# red