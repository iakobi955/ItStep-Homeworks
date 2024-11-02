# 1. დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), 
# თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; 
# თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. 
# მიღებული შედეგი დაბეჭდეთ კონსოლში.

# a – append
# r – remove
# e – exit

# გამოიყენეთ მხოლოდ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.


from random import randint

arr = []

while True:
    add_digits = input("Please enter a character: a _ append, r _ remove, e _ exit: ")
    if add_digits == "a":
        arr.append(randint(1,100))
        print(arr)
    elif add_digits == "r":
        arr.remove(arr[-1])
        print(arr)
    elif add_digits == "e":
        break
    else:
        print("Incorect character")
        print(arr)

print("\nDone")
print(arr)