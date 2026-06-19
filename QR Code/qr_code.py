import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

try:
    print("=" * 50)
    print("QR CODE GENERATOR AND DECODER")
    print("=" * 50)
    print("1. Generate QR Code")
    print("2. Decode QR Code")
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        # GENERATE QR CODE
        qr_url = input("Enter URL or Text to Generate QR Code: ")
        qr_name = input("Enter Name to Save QR Code (without extension): ")

        if not qr_url:
            raise ValueError("URL or Text cannot be empty.")
        if not qr_name:
            qr_name = "my_qrcode"

        img = qrcode.make(qr_url)
        img.save(f"{qr_name}.png")
        print(f"✓ QR Code saved as {qr_name}.png")
    
    elif choice == '2':
        # DECODE QR CODE
        qr_file = input("Enter QR Code filename to decode: ")
        
        img = Image.open(qr_file)
        
        decoded_objects = decode(img)
        
        if decoded_objects:
            for obj in decoded_objects:
                print(f"\n✓ QR Code Decoded Successfully!")
                print(f"Type: {obj.type}")
                print(f"Data: {obj.data.decode('utf-8')}")
        else:
            print("✗ No QR code found in the image.")
    
    else:
        print("Invalid choice! Please enter 1 or 2.")

except FileNotFoundError:
    print("✗ Error: File not found. Please check the filename.")
except Exception as e:
    print(f"✗ An error occurred: {e}")