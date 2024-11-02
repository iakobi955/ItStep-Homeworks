# TODO
# დაწერეთ პროგრამა, რომელიც ტერმინალში მომხმარებელს გამოუტანს სტუდენტების აიდის (id) სიას, 
# მომხარებელი აირჩევს სტუდენტის აიდის, მიიღებული აიდისთვის დაბეჭდავს სტუდენტის მონაცემებს. 
# მონაცემებში უნდა დაიბეჭდოს (სახელი, გვარი, ასაკი და ქულა თითოეული საგნის მიხედვით)

# მაგალითად: მომხარებელმა თუ აირჩია სტუდენტი აიდით 20, უნდა დაბეჭდოთ ამ სტუდენტის ინფომრაცია.

# terminal ouput: 
# studentebis ID: 20, 25, 100, 56, 1232, 846723
# airchiet studentis ID: 
# შემდეგ მომხარებელს შეყავს აიდი, მაგალითად  - 20 

# თქვენ ბეჭდავთ ტერმინალში შემდეგ ინფორმაციას output:

# student infomration:
# ID: 20, Name: Giorgi, Age: 25
# subject: Math, grade: B
# subject: Physics, grade: A
# subject: English, grade: A
# subject: Chemistry, grade: B
# subject: History, grade: c


my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}

input_ID = input('studentebis ID: 20, 25, 100, 56, 1232, 846723\nairchiet studentis ID:')
print()

for x in my_dict.get('students'):

    st_id = str(x['id'])

    if input_ID == st_id:
        
        st_id = input_ID
        st_name = x['name']
        st_age = x['age']
        print(f"student infomration:\nID: {st_id}, Name: {st_name}, Age: {st_age}")

        for grade in my_dict.get('subjects'):

            subj = grade['name']
            st_grade = grade.get('grades').get(st_id)

            print(f"sunject: {subj}, grade: {st_grade}")
        
        print()
