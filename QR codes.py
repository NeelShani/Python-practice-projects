import pyqrcode 
from pyqrcode import QRCode 
  
# Asking for link of webpage which will open using qr code 
src = input("Please enter link for QR Code- ")

  
# Generate QR code 
url = pyqrcode.create(src) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myGitHub.svg", scale = 8) 