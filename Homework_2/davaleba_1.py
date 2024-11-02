# 1. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით 
# # დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.
# მაგ.:
# Enter a number: 56
  
# The number in list

# #===========================

# Enter a number: 45
  
# The number not in list

num_list = [44, 23, 11, 8, 20, 56, 33, 55]
number = int(input("Enter a number: "))

if number in num_list:
    print("The number in list")
else:
    print("The number not in list")