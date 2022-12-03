import string

line = str(input("Введите строку:"))
string.punctuation

for i in string.punctuation:
    if i in line:
        line = line.replace(i, "")

print(line.lower())
print(type(line))
