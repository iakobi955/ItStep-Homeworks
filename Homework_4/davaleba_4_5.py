# 5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს,
# სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი
# გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.


import base64

st = input('Enter a string: ')

st_64 = base64.b64encode(st.encode('utf-32'))
print(st_64)

st = base64.b64decode(st_64).decode('utf-32')
print(st)