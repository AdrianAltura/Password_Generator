#Password Generator Project
import random
# import string_utils

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!92

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ''

nr_letters = input("How many letters would you like in your password?\n")
if nr_letters.isnumeric():
  x = int(nr_letters)
  for i in range(x):
    password += random.choice(letters)
    
  nr_symbols = input("How many symbols would you like?\n")
  if nr_symbols.isnumeric():
    y = int(nr_symbols)
    for i in range(y):
      password += random.choice(symbols)
      
    nr_numbers = input("How many numbers would you like?\n")
    if nr_numbers.isnumeric():
      z = int(nr_numbers)
      for i in range(z):
        password += random.choice(numbers)

      # This method works also:  
      # x = string_utils.shuffle(password)
      x = ''.join(random.sample(password,len(password)))
      print(f'Your password is: {x}')
      
    else:
      print('Invalid Entry. Please input a number!')
      
  else:
    print('Invalid Entry. Please input a number!')
    
else:
  print('Invalid Entry. Please input a number!')

