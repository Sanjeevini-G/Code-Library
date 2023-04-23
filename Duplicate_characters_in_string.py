string = "Hello World"
duplicates = []

for char in string:
    if string.count(char) > 1 and char not in duplicates:
        duplicates.append(char)

print("Duplicate characters in the string:", duplicates)
