text = input("Enter a number or text: ")
text = text.lower()

if text == text[::-1]:
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")