# 1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n,
#    და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.

def func1(n):
    arr1 = [0, 1]

    for i in range(2, n):
        arr1.append(arr1[-1] + arr1[-2])
        
    return arr1
        
#=================


print(func1(12), "\n")