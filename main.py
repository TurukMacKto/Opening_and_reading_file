#with open('recipes.txt', encoding='utf-8') as text:
   #print(text)
file = open('recipes.txt', encoding='utf-8')
#print(file.read(5))
#print(file.read(53))
#print(file.read(5))
print(file.readlines())
#for row in file:
    #print(row)
    #for letter in row:
        #print(letter)
s = file.readlines(1)
w = file.readlines(1)
print(s)
print(w)
#print(next(file), next(file))
#for row in file:
    #print(row.strip())
