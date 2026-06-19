def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_ammount = ord(char) + shift
            if char.islower():
                if shift_ammount > ord('z'):
                    shift_ammount -= 26
                result += chr(shift_ammount)
            elif char.isupper():
                if shift_ammount > ord('Z'):
                    shift_ammount -= 26
                result += chr(shift_ammount)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("=" * 60)
print("1. Encrypt")
print("2. Decrypt")
print("=" * 60)

choice = input("Enter your choice (1/2): ")

message = input("Enter the message : ")
shift = int(input("Enter the shift value : "))

if choice == '1':
    print("Encrypted Message: ", encrypt(message, shift))

elif choice == '2':
    print("Decrypted Message: ", decrypt(message, shift))
          
else:
    print("Invalid choice! Please choose either 1 or 2.")