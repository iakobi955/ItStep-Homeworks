# 2. პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე, 
#    რომლის შეცვლაც შეუძლებელი იქნება (frozenset).

arr = frozenset(map(eval, input("Enter a sequence: ").split()))

print(arr)