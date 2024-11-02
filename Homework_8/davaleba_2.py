# 2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და 
#    შეამოწმებს არის თუ არა სტრიქონები ანაგრამები (ანაგრამი არის სიტყვა ან შესიტყვება,
#    რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.


def my_func(string1, string2):
    if sorted(string1) == sorted(string2):
        print("It's anagrama\n")

    else:
        print("It's mnot anagrama\n")

my_func("race", "care")