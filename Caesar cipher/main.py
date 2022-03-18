Alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# importing art
from art import logo
print(logo)


# defining the logic

def caeser_cipher(start_text,shift_amount,cipher_direction):
  final_text=""
  if cipher_direction == "decode":
      shift_amount *= -1  
  for char in start_text:
    if char in Alphabets:
     position = Alphabets.index(char)
     final_text += Alphabets[position+(shift_amount)]
    else:
      final_text += char
  print(f"The {cipher_direction}d text is {final_text}")
  


# looping untill the user preference
repeat = True
while repeat:
  direction = input("Type encode for \"Encode\" and \"Decode\" for decrypt: \n").lower()
  text = input("Enter your secrect message:\n ").upper()
  shift_no = int(input("Type the shift number:\n "))
  shift = shift_no%26
  caeser_cipher(start_text = text,shift_amount=shift,cipher_direction=direction) 
  result = input("Do u want to go again type\'Y\'or to stop type\'N\'\n").lower()
  
  if result =="n":
   repeat =False
   print("Thank you for using caesar ciper")
    
