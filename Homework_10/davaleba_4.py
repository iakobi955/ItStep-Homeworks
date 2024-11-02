# 4. დაწერეთ პითონის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). 
#    დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. 
#    გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), 
#    თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.

#    მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, 
#              რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

# params: ['hello', 'world', 'coding', 'nod'], 'ing'  
# outputs: ['coding']

arr1 = ['hello', 'world', 'coding', 'nod']
ending = 'ing'

try:
    my_res = list(filter(lambda x: x.endswith(ending), arr1))

    print(my_res)
except TypeError as err:
    print(err)
except Exception as ex:
    print("!!! Other Error!!!")