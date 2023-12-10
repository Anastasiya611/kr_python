import os
from data_create import name_data, id_data, info_data, time_data

file_name = "data.csv"
def print_data():
    if os.path.exists(file_name):
        print("Ваши заметки:")
        with open(file_name, "r", encoding="utf-8") as file:
            list_data = file.readlines()
            for element in list_data:
                print(element)
    else:
        print("файла не существует")

def input_data():
    print("Введите данные для записи в файл:")
    name = name_data()
    id = id_data()
    info = info_data()
    time = time_data()

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{name};{id};{info};{time};\n")


def delete_data():
    with open(file_name, "r", encoding="utf-8") as file:
        delete_data = file.readlines()
        delete_string = input("введите строку для удаления ")
        with open(file_name, "w", encoding="utf-8") as file:
            for delete in delete_data:
                if delete_string in delete:
                    print("Данные удалены:")
                else:
                    print(delete)
                    file.write(delete)

def new_data():
    with open(file_name, "r", encoding="utf-8") as file:
        list_data = file.readlines()        
        string = input("введите строку для изменения ")
        with open(file_name, "a", encoding="utf-8") as file:
            new_string = input("Введите новые данные ")
            for element in list_data:
                if string in element:
                    new_list = element.replace(string,new_string)
                    list_data = new_list
            file.write(list_data)
            delete_data()
