# 5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია,
#    რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის 
#    შებრუნებულ (revers) სტრიქონს (მაგალითად  input: Hello   Output: olleH)

def my_func(string):

    if len(string) <= 1:
        return string
    
    else:
        return string[-1] + my_func(string[:-1])


#=================
print(my_func("Hello"))