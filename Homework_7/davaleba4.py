# 4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple).
#    დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით (list).


# გრძელი მეთოდი

# my_tuple = tuple(map(eval, input("Enter a sequence: ").split()))
# print(my_tuple)

# unic_elem = set(my_tuple)
# print(unic_elem)

# my_list = list(unic_elem)
# print(my_list)

#მოკლე მეთოდი

my_list = list(set(tuple(map(eval, input("Enter a sequence: ").split()))))
print(my_list)