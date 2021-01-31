#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#letters

# password = ""

# for char in range(1,nr_letters +1 ):
#   password+= random.choice(letters)

# for char in range(1,nr_symbols +1 ):
#   password+= random.choice(symbols)

# for char in range(1,nr_numbers +1 ):
#   password+= random.choice(numbers)

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password = ""

# choice = random.randint(0,2)
# total_len += nr_letters
# # letters for 1, symbols for 2, numbers for 3

# for alpha in range(0,nr_letters): 
#   ran_alpha = random.randint(0,len(letters)-1)
#   password += letters[ran_alpha]
# # print(password)

# #symbols

# for sym in range(0,nr_symbols): 
#   ran_sym = random.randint(0,len(symbols)-1)
#   password += symbols[ran_sym]

# #number
# for num in range(0,nr_symbols): 
#   ran_num = random.randint(0,len(numbers)-1)
#   password += numbers[ran_num]

# new_pass =""
# new_choice = random.randint()



# print(new_pass)

password = []

for char in range(1,nr_letters +1 ):
  password+= random.choice(letters)

for char in range(1,nr_symbols +1 ):
  password+= random.choice(symbols)

for char in range(1,nr_numbers +1 ):
  password+= random.choice(numbers)

new_password = ""

# for char in password:
#   new_password += random.choice(password)
random.shuffle(password)


for char in password:
  new_password += char


print(new_password)
