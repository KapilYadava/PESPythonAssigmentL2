# Apply all built in functions on Strings in your program.
# Note: There are 40 string functions.
# Use Tutorial for the help. Note: Each program should have 5 string built in functions
# (so write 8 programs to cover all string functions)

string1 = 'this is my'
string2 = 'India'

print(string1 + " " + string2)  # appending two strings
print("This is my {}".format(string2))  # formatting strings
print(string1.index(string1[4:]))  # finding start index of substring into given string
print(string1.split(" "))  # split string using spaces or comma
print(string1.count('i'))  # count chars and substring ocurrence

print('*' * 100)

print(string1.title())  # return title case version of string
print(string1.capitalize())  # return capitalized string make first char capital case.
print(string1.casefold())  # return case less comparison string
print(string1.center(25, 'a'))  # return centered string by filling char
print(string1.find('is my'))  # Return the lowest index in S where substring sub is found

print('*' * 100)

print(string1.endswith("my"))  # check whether string endwith substring
print(string1.startswith('is'))  # check weather string startwith substring
print(string1.isdigit())  # # check weather string is digits
print(string1.isalpha())  # check weather string is having alphanumeric chars
print(string1.islower())  # check weather string is in lower case
print(string1.isupper())  # check weather string is in uppercase

print('*' * 100)

print(string1.isalnum())  # check whether string having only alphanumeric chars
print(string1.isdecimal())  # check weather string having only decimal chars
print(string1.isnumeric())  # # check weather string having only numeric chars
print(string1.isspace())  # check weather string is having all whitespaces
print(string1.isprintable())  # check weather string is printable

print('*' * 100)

print(string1.isidentifier())  # check whether string is a valid identifier according to the language definition.
print(string1.istitle())  # check weather string is title case string
print(string1.join("help"))  # check weather string having only numeric chars
print(string1.rjust(20, 'a'))  # check weather string is having all whitespaces
print(string1.ljust(20, 'a'))  # check weather string is printable
