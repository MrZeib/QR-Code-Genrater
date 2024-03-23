import qrcode as qr
from random import randint

try:
  user_string: str = input("Enter Text or 'q' to Quit: ")
  if user_string == "q":
    print("\nExiting the Program\n")
    exit()
  else:
    qr_code = qr.make(user_string)
    qr_name_input = input("Enter Name of Your Qr Code: ")
    qr_name = f"{qr_name_input}.png"
    qr_code.save(qr_name)
    print(f"Qr Code Seccesfully Genrated.\nYour Qrcode Name is: {qr_name}")
except KeyboardInterrupt:
  print("\nExiting the Program\n")
  exit()S
