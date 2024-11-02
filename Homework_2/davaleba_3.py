# 3. შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, 
# თუ ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"


str1 = "Koba samnashvili"
str2 = "Koba"

if str1 is str2:
    print("Same object")
else:
    print("Different object")