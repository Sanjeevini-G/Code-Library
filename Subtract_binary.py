def subtract_binary(a, b):
    # Pad the binary numbers with leading zeros to ensure they have the same length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Convert the binary numbers to decimal and subtract them
    diff = int(a, 2) - int(b, 2)

    # Convert the result back to binary and return it
    return bin(diff)[2:]

# Example usage of subtract_binary
a = "1010"
b = "0110"
result = subtract_binary(a, b)
print(result)    # prints "1000"
