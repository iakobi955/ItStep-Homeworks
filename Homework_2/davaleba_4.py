# 4. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:
# * თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";
# * თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";
# * სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
# რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.
# მაგ.:

# Enter a number: 105
# None of the conditions were met

# #===========================
# Enter a number: 40
# More than list elements

# #===========================
# Enter a number: 56
# Equal

num_list = [44, 23, 11, 8, 20, 56, 33, 55]
number = int(input("Enter a number: "))

if number > num_list[2] and number < num_list[-1]:
    print("More than list elements")
elif number == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")