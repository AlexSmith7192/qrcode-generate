import qrcode

# Data that we want to transform into QR Code
data = {
 "link1": "https://www.google.com",
 "link2": "https://www.python.org",
 "link3": "https://www.youtube.com",
 }

# Creation of the QR Code object
qr = qrcode.QRCode(
 version=1, # control the size of the QR Code
 error_correction=qrcode.constants.ERROR_CORRECT_H, # error correction level
 box_size=10, # size of each "box" in the QR Code
 border=4, # border around the QR Code
)

for link in data:
 # Adding data to QR Code
 qr.add_data(data[link])
 qr.make(fit=True)

 # Creating the QR Code image
 img = qr.make_image(fill='black', back_color='white')

 # Saving the image to a file
 img.save(f"./qr_codes/{link}.png")
 qr.clear()

print("QR Code generated and saved successfully")