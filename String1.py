# Write a program to print the different data types (Numbers, strings characters)
#  using the Format symbols (Refer to different format symbols specified in Tutorial)

country = "India"
num_of_state = 30

print('We have {} states in {}'.format(num_of_state, country))

# Receive the encoded string from your friend & decode it to check the original message.
# PS: You will receive Encoded string and the Algorithm used for encoding.

import base64

print('*' * 100)
original = "This is me hidden by secured algorithm"
print("Original String: " + original)
encoded = original.encode('utf-8', errors='strict')
encoded_string = base64.b64encode(encoded)
print('Encoded String: ' + str(encoded_string))

decoded_string = base64.b64decode(encoded_string)
decoded = decoded_string.decode()
print('Decoded String: ' + decoded)

# Write a program to check given string is Palindrome or not.
# That is reverse the given string and check whether it is same as original string, if so then it is palindrome.
# Example: String = "malayalam"  reverse string = "malayalam" hence given string is palindrome.
# Use built functions to check given string is palindrome or not.

print('*' * 100)
language = "malayalam"
reverse = language[::-1]
if language == reverse:
    print("{} string is palindrome".format(language))
else:
    print("{} string is not palindrome".format(language))

# Write a program to check how many ovals present in the given string.
# That is, count the number of " a e i o u" in the given string and print the numbers against each oval.
# Example:- "This is Python" Number of total ovals = 3, i = 2, o =1

print('*' * 100)

l = list()
string = "This is Python"
vowels = 'aAeEiIoOuU'

for char in string:
    if char in vowels:
        l.append(char)

print(l)
