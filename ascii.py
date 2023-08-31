def text_to_hex(text):
    hex_values = ' '.join(format(ord(char), '02X') for char in text)
    return hex_values

input_text = input("Enter the text to convert to hexadecimal: ")
hex_output = text_to_hex(input_text)
print("Hexadecimal values:", hex_output)