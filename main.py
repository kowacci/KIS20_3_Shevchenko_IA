import string
line = string
def replace_symbols(line):
        string.punctuation
        line = str(input("Введите строку:"))
        for i in string.punctuation:
            if i in line:
                line = line.replace(i, "")
        return line
print(replace_symbols(line))