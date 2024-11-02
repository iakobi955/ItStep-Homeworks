# 2. დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list_1 = [43, '22', 12, 66, 210, ["hi"]], 
#    და შეასრულებს შემდეგ ნაბიჯებს:

# a. დაბეჭდავს 210-ის ინდექსს;
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello";
# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
# d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist_1-ის მნიშვნელობა, 
#    გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.

# მინიშნება: სიის გასუფთავება – arr.clear()

my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

print("1)")
print(my_list_1.index(210))
print()

print("2)")
my_list_1[-1].append("hello")
print(my_list_1)
print()

print("3)")
del my_list_1[2]
print(my_list_1)
print()

print("4)")
my_list_2 = my_list_1[:]
my_list_2.clear()
print(my_list_1)
print(my_list_2)

print("Done")