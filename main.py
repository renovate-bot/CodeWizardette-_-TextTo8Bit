def text_to_8bit(filename):
    with open(filename, 'r') as file:
        text = file.read()
    binary_data = ' '.join(format(ord(char), '08b') for char in text)
    return binary_data
input_filename = 'CevirilecekMetinDosyasiYolu.txt'
eight_bit_data = text_to_8bit(input_filename)
eight_bit_output_filename = '8bitVeri.txt'
with open(eight_bit_output_filename, 'w') as output_file:
    output_file.write(eight_bit_data)
print(f"Metnin 8 bitlik hali dosyaya kaydedildi: {eight_bit_output_filename}")
