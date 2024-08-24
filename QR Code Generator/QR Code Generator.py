import qrcode as qr # importing the qrcode module
img = qr.make("https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools.html")   # Creating the QR-Code as Image
img.save("AMD Vivado ML.png")   # Saving the QR as a png file

