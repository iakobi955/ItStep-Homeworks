# 2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# ჩამოაშორეთ ზედმეტი ინტერვალები.
# ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და
# დაუმატეთ ქვესტრიქონი 'Python'.
# თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.

# მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია `.strip()`.

# მაგ.: "  Python is funny     ".strip()   ====>  "Python is funny"


st = input("Enter a string: ")

st = st.strip()
st = st.lower()

if "python" in st:
    print(st.replace('python', 'Python'))

else:
    print(st + ' Python')