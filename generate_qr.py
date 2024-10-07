import qrcode

# URL to the KBC game (this will be the HTML file we create)
game_url = "https://atharvn07.github.io/KBC_game/"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(game_url)
qr.make(fit=True)

# Save the QR code as an image
img = qr.make_image(fill='black', back_color='white')
img.save("kbc_qr_code.png")

print("QR code generated and saved as kbc_qr_code.png.")
