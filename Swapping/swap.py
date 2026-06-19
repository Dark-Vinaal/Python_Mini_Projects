char1 = input("Enter character 1: ")
char2 = input("Enter character 2: ")

print("\nBefore swapping characters")
print("\nCharacter 1 =", char1)
print("Character 2 =", char2)

print("\n", char1, char2)

char1, char2 = char2, char1

print("\nAfter swapping characters")
print("\nCharacter 1 =", char1)
print("Character 2 =", char2)

print("\n", char1, char2)