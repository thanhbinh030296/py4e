#exercise 4
file = open('romeo.txt')
list_words = []
for line in file:
    words = line.split()
    #print(line)
    for word in words:
        try:
            list_words.remove(word)
        except:
            k = 1  
        list_words.append(word)
print(list_words)
print("\nSorted:\n")
list_words.sort()
print(list_words)