# 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს 
# და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.

st = input("Enter a string: ")

st1 = st.encode("utf-8")

print(st1)