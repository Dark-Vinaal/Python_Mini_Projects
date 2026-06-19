import qrcode

try:
    qr_url = input("Enter URL or Text to Generate QR Code : ")
    qr_name = input("Enter Name to Save QR Code (without extension) : ")

    if not qr_url:
        raise ValueError("URL or Text cannot be empty.")
    if not qr_name:
        qr_name = "my_qrcode"

    img = qrcode.make(qr_url)
    
    img.save(f"{qr_name}.png")
    print(f"QR Code saved as {qr_name}.png")

except Exception as e:
    print("An error occurred : ", e)
    
