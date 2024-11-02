# 3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.

def my_func(n):

    fact = 1
    for i in range(1, n+1):
        fact *=i

    return fact

print(my_func(5))