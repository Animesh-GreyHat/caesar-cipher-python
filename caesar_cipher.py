def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


if __name__ == "__main__":
    print("🔐 Caesar Cipher Tool")
    message = input("Enter message: ")
    shift = int(input("Enter shift value: "))

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nEncrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
