import base64

def encrypt(password):
    """Encode a string to base64"""
    encoded_bytes = base64.b64encode(password.encode())
    return encoded_bytes.decode()

def decrypt(encoded_string):
    """Decode a base64 string"""
    decoded_bytes = base64.b64decode(encoded_string)
    return decoded_bytes.decode()

def main():
    """Interactive CLI for encoding/decoding"""
    print("=" * 50)
    print("    BASE64 ENCODER/DECODER TOOL")
    print("=" * 50)

    while True:
        print("Choose an option:")
        print("1. Encrypt (Encode) a string")
        print("2. Decrypt (Decode) a string")
        print("3. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            text = input("Enter the text to encrypt: ")
            try:
                encrypted = encrypt(text)
                print(f"✅ Encrypted/Encoded: {encrypted}")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            text = input("Enter the base64 string to decrypt: ")
            try:
                decrypted = decrypt(text)
                print(f"✅ Decrypted/Decoded: {decrypted}")
            except Exception as e:
                print(f"❌ Error: Invalid base64 string!")

        elif choice == "3":
            print("👋 Thank you for using Base64 Encoder/Decoder!")
            break

        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
