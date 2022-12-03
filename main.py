import string

def replace_symbols(line):
    string.punctuation
    for i in string.punctuation:
        if i in line:
            line = line.replace(i, "")
    return line
line = str(input("Введите строку:"))

print(replace_symbols(line))
