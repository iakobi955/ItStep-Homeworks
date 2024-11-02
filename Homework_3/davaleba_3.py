# 3. დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად 
# სთხოვს მომხმარებელს გამოიცნოს წინასწარ განსაზღვრული რიცხვი. 
# როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.

from random import randint
num = randint(1, 50)

cda = 5

while cda > 0:
    guess = int(eval(input(f"gamoicaniT ricxvi 1-dan 50 -is CaTvliT, dargrCaT {cda} cda: ")))
    if guess == num:
        print("gilocavT, Tqven gamoicaniT Cafiqrebuli ricxvi")
        break
    elif guess > num:
        print("მეტია")
    else:
        print("ნაკლებია")
    
    print()
    
    cda -=1

print(f"Game over, guessed number was {num}")
