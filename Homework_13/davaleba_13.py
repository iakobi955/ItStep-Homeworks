# შექმენით csv  ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:

# id,name,age,grade,subject_name,mark
# 1,string,0,string,string,0
# 2,string,0,string,string,0

# 1. დაწერეთ პითონის ფუნქცია, სადაც მომხარებელი შეიყვანს ინფორმაციას
#    (id,name,age,grade,subject_name,mark) და თქვენ სტუდენტს დაამატებს csv ფაილში.
#    დაასორტირეთ მონაცემები id-ის მიხედვით.
# 2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება,
#    როგორც ყველა, ასევე კონკრეტული სტუდენტის ინფორმაციის წაკითხვა ფაილიდან.
# 3. დაწერეთ პითონის ფუნქცია, რომელიც დაითვლის საშუალო ქულას (marks) საგნების მიხედვით.
# 4. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის 
#    განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის id, საგანს და განახლებულ ქულას.

import os, csv

folder = "files"
fileName = "data.csv"
os.makedirs(folder, exist_ok= True)
fileName = os.path.join(folder, fileName)

def create_csv_file():
    with open(fileName, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def add_student(id, name, age, grade, subject_name, mark):
    with open(fileName, 'a', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'id': id, 'name': name, 'age': age, 'grade': grade, 'subject_name': subject_name, 'mark': mark})

    with open(fileName, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        sortedlist = sorted(reader, key=lambda x: int(x['id']))

    with open(fileName, 'w', newline='', encoding="utf-8") as file:
        fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in sortedlist:
            writer.writerow(row)

def read_students(student_id=None):
    with open(fileName, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if student_id:
            for row in reader:
                if int(row['id']) == student_id:
                    print(row)
        else:
            for row in reader:
                print(row)

def calculate_average_marks_by_subject():
    subject_marks = {}

    with open(fileName, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            subject = row['subject_name']
            mark = int(row['mark'])
            if subject in subject_marks:
                subject_marks[subject].append(mark)
            else:
                subject_marks[subject] = [mark]

    for subject, marks in subject_marks.items():
        average = sum(marks) / len(marks)
        print(f"Average mark for {subject}: {average}")

def update_student_mark(student_id, subject_name, new_mark):
    with open(fileName, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

    for row in rows:
        if int(row['id']) == student_id and row['subject_name'] == subject_name:
            row['mark'] = new_mark
            break

    with open(fileName, 'w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

#===================================
create_csv_file()

add_student(3, 'Giorgi', 16, '10', 'History', 78)
add_student(1, 'Mari', 18, '12', 'Math', 12)
add_student(2, 'Nini', 17, '11', 'Science', 92)

print()
print("Read All Students:")
read_students()

print()
print("Print current Student:")
read_students(2)

print()
print("Print Average Marks:")
calculate_average_marks_by_subject()

update_student_mark(1, 'Math', 90)