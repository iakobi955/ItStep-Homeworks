# 1. დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის საქაღალდის მისამართს, ფაილის სახელს და შემქნის მას.
# 2. დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს.
# 3. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.
# 4. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და ჩაწერს/გაანახლებს ფაილის კონტენტს.

# p.s. ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია.

import json
from pprint import pp

def create_json_file(path, file):
    file_path = f"{path}/{file}.json"

    try:
        with open(file_path, mode='x', encoding='utf-8'):
            ...
    except FileExistsError:
        print(f"File '{file_path}' already exists!")

    return file_path

def write_data_json_file(path, json_data):
    with open(path, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(json_data, indent=2))

def read_json_file(path):
    with open(path, mode='r', encoding='utf-8') as file:
        return json.loads(file.read())

def update_json_file(path, json_data):
    data = read_json_file(path)

    for st in data:
        if st['id'] == json_data['id']:
            break
    else:
        data.append(json_data)
        data.sort(key= lambda x: x['id'])

        write_data_json_file(path, data)

    return data

#=======================

chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

file_path = create_json_file("files/jsons", "data")

write_data_json_file(file_path, chess_players)

new_players = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

for st in new_players:
    data = update_json_file(file_path, st)

pp(data)