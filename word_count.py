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

print(book.keys()) # prints dict_keys(['red', 'blue', 'green'])
print(book.items()) # prints dict_items([('red', 4), ('blue', 2), ('green', 2)])

# Another way to print each word with the number of times it appears
for word, count in book.items():
    print(f"'{word}': {count} time(s)")

# test values:
# red
# red
# red
# blue
# green
# blue
# green
# red
    
    