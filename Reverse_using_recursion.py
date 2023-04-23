def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

string = "Hello World"
print("Original string:", string)

reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)
