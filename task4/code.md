# Text Compression Using Character Runs – Python Program

## 1. Problem Statement

Write a Python program to perform text compression using Run-Length Encoding (RLE).

The program should:

- Read a string from the user.
- Group consecutive repeated characters.
- Encode each group using the character followed by its count.
- Calculate the original and compressed string lengths.
- Compare both lengths.
- If the encoded string is not shorter than the original string, display the original string as the better option.

## 2. Algorithm

1. Start the program.
2. Read a string from the user.
3. Initialize an empty encoded string.
4. Set the count of the first character to 1.
5. Compare each character with the next character.
6. If both characters are the same, increase the count.
7. Otherwise, add the character and its count to the encoded string.
8. Repeat until all characters are processed.
9. Calculate the original and encoded string lengths.
10. Compare both lengths.
11. If encoded length is smaller, display the compressed string.
12. Otherwise, display the original string.
13. Stop the program.

## 3. Python Source Code

```
# Text Compression Using Character Runstext = input("Enter a string: ")encoded = ""count = 1for i in range(1, len(text)):    if text[i] == text[i - 1]:        count += 1    else:        encoded += text[i - 1] + str(count)        count = 1# Add the last character groupif len(text) > 0:    encoded += text[-1] + str(count)original_length = len(text)encoded_length = len(encoded)print("Original String:", text)print("Encoded String:", encoded)print("Original Length:", original_length)print("Encoded Length:", encoded_length)if encoded_length < original_length:    print("Compression is beneficial.")    print("Compressed Text:", encoded)else:    print("Compression is not beneficial.")    print("Better Text:", text)
```

## 4. Sample Input

```
Enter a string: aaabbbccccdd
```

## 5. Sample Output

```
Original String: aaabbbccccdd
Encoded String: a3b3c4d2
Original Length: 12
Encoded Length: 8
Compression is beneficial.
Compressed Text: a3b3c4d2
```

## 6. Flowchart
```mermaid

flowchart TD
    A([Start]) --> B[/Enter a string/]
    B --> C[Initialize encoded = empty, count = 1]
    C --> D[Set i = 1]
    D --> E{i < length of string?}
    E -- Yes --> F{Current character equals previous?}
    F -- Yes --> G[Increase count]
    F -- No --> H[Add previous character and count to encoded]
    H --> I[Set count = 1]
    G --> J[Increase i]
    I --> J
    J --> E
    E -- No --> K[Add last character and count]
    K --> L[Calculate original and encoded lengths]
    L --> M{Encoded length < original length?}
    M -- Yes --> N[/Display compressed string/]
    M -- No --> O[/Display original string/]
    N --> P([Stop])
    O --> P
```
flowchart TD
    A([Start]) --> B[/Enter a string/]
    B --> C[Initialize encoded = empty, count = 1]
    C --> D[Set i = 1]
    D --> E{i < length of string?}
    E -- Yes --> F{Current character equals previous?}
    F -- Yes --> G[Increase count]
    F -- No --> H[Add previous character and count to encoded]
    H --> I[Set count = 1]
    G --> J[Increase i]
    I --> J
    J --> E
    E -- No --> K[Add last character and count]
    K --> L[Calculate original and encoded lengths]
    L --> M{Encoded length < original length?}
    M -- Yes --> N[/Display compressed string/]
    M -- No --> O[/Display original string/]
    N --> P([Stop])
    O --> P
```

## 7. Another Example (Compression Not Beneficial)

Sample Input:

```
Enter a string: abcdef
```

Sample Output:

```
Original String: abcdef
Encoded String: a1b1c1d1e1f1
Original Length: 6
Encoded Length: 12
Compression is not beneficial.
Better Text: abcdef
```

Conclusion: Run-Length Encoding reduces the text size when many consecutive characters are repeated. If the encoded string is longer, the original string is better.
