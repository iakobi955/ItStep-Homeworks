# 2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას.
# თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.

# მაგ.:

# Enter an integer: 25
  
# The number is odd

# #===========================

# Enter an integer: 36
  
# The number is even


integer = int(input("Enter a integer: "))
if (integer % 2) == 1:
    print("The number is odd")
else:
    print("The number is even")