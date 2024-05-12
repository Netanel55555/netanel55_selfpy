def isPalindrom(str):
    return str == str[::-1]

input_string = input("Enter a word: ")

if isPalindrom(input_string):
    print("OK")
else:
    print("NOT")
