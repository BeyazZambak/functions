documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
    }

def people(documents, number):
    count = 0
    for folder in documents:
        count += 1
        if len(documents) < count:
            if folder["number"] == number:
                print(f'Имя владельца документа: {folder["name"]}')
        else: 
            print('Такого документа нет')

def shelf(directories, number):
    for directory, numbers in directories.items():
        if numbers.count(number) == True:
            print(f'Этот документ лежит на полке {directory}')
    else:
        print("Такого документа нет ни на одной полке")

def list(documents):
    for document in documents:
        print(document.get("type"), document.get("number"), document.get("name"))

def add(documents, directories):
    type = input("Уточните тип документа: ")
    number = input("Уточните номер документа: ")
    name = input("Уточните владельца документа: ")
    direct = input("Уточните номер полки, на которую нужно положить документ: ")
    for directory in directories:
        count = 0
        if len(directories) > count:
            count += 1
            if direct == directory:
                dict = {"type": type, "number": number, "name": name}
                documents.append(dict)
                directories[direct] = number 
        else:
            print("Такой полки не существует!!!")

def program():
    while 1 == 1:
        document = ''
        comand = str(input("Введите команду p / s / l / a : "))
        print(comand)
        if comand == 'p':
            document = input("Введите номер документа: ")
            people(documents, document)
        elif comand == 's':
            number = input("Введите номер документа: ")
            shelf(directories, number)
        elif comand == 'l':
            list(documents)
        elif comand == 'a':
            add(documents, directories)
        else:
            print("Нет такой команды")
program()