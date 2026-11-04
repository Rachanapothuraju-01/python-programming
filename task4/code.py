
# Text Compression Using Character Runs

text = input("Enter a string: ")

encoded = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        encoded += text[i - 1] + str(count)
        count = 1

# Add the last character group
if len(text) > 0:
    encoded += text[-1] + str(count)

original_length = len(text)
encoded_length = len(encoded)

print("Original String:", text)
print("Encoded String:", encoded)
print("Original Length:", original_length)
print("Encoded Length:", encoded_length)

if encoded_length < original_length:
    print("Compression is beneficial.")
    print("Compressed Text:", encoded)
else:
    print("Compression is not beneficial.")
    print("Better Text:", text)

