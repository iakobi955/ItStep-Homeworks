# 1. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" 
# და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს.

sum = 0
number = int(input("SeiyvaneT ricxvi: "))

for i in range(number):

    sum += i
    
print(f"1-dan {number}-mde ricxvebis jami aris: {sum}")