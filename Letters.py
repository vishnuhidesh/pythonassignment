def list_of_frequency(input_string):
    letter_frequency = {}
    for char in input_string:
        if char.isalpha():
            if char in letter_frequency:
                letter_frequency[char] += 1
            else:
                letter_frequency[char] = 1
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)
    print("Letter frequencies:")
    print(letter_frequency)
    print("Letters in non-increasing order of frequency:")
    for letter, frequency in sorted_frequency:
        print(f"('{letter}', {frequency})", end=" ")

input_string = input("Enter a string: ")
list_of_frequency(input_string)
