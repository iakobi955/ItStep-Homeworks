# 4. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0, 
# შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. 
# ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, 
# რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.

total_sum = 0
 
while True:
    num = input("SeiyvaneT ricxvebi, dasajameblad SeiyvaneT 'sum' teqsti: ")
    if num == "sum":
        print(f"ricxvTa jami aris: {total_sum}")
        break
    else:
        total_sum += int(num)