from logger import input_data, print_data, delete_data, new_data
def interface():
    print ("""Выберите режим работы:
            1 - запись данных,
            2 - вывод данных,
            3 - удаление данных
            4 - изменение данных
            """)
    command_number = int (input("Введите номер команды "))
    while command_number < 1 or command_number > 5:
        print ("Введите корректный номер команды")
        command_number = int (input("Введите номер команды"))

    if command_number == 1:
        input_data()
    elif command_number == 2:
        print_data()
    elif command_number == 3:
        delete_data()
    elif command_number == 4:
        new_data()
           
