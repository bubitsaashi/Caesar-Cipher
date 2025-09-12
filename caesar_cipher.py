def caesar_encrypt(text: str, shift: int) -> str:
    shift = shift % 26
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            # map 'a'..'z' -> 0..25, shift, then back
            new_ord = (ord(ch) - ord('a') + shift) % 26 + ord('a')
            result.append(chr(new_ord))
        elif 'A' <= ch <= 'Z':
            new_ord = (ord(ch) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(new_ord))
        else:
            # preserve punctuation, spaces, digits, etc.
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text: str, shift: int) -> str:
    # decryption is encryption with negative shift
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher — encrypt/decrypt")
    while True:
        choice = input("\nChoose: (E)ncrypt, (D)ecrypt, (Q)uit: ").strip().lower()
        if choice == 'q' or choice == 'quit':
            print("Goodbye!")
            break
        if choice not in ('e', 'encrypt', 'd', 'decrypt'):
            print("Please enter E, D, or Q.")
            continue

        text = input("Enter the message: ")
        shift_input = input("Enter shift (integer, e.g. 3): ").strip()
        try:
            shift = int(shift_input)
        except ValueError:
            print("Shift must be an integer. Try again.")
            continue

        if choice.startswith('e'):
            output = caesar_encrypt(text, shift)
            print("\nEncrypted message:")
        else:
            output = caesar_decrypt(text, shift)
            print("\nDecrypted message:")

        print(output)

if __name__ == "__main__":
    main()
