# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. 
#    ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
#    ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.  

# params:[1, 2, 3, 4, 5] 
# output: 120

from functools import reduce

arr1 = [1, 2, 3, 4, 5]

try:
    my_result = reduce(lambda x, y: x*y, arr1)
    print(my_result)

except TypeError as err:
    print(err)


