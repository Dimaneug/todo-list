def read_tasks():
    tasks = []
    with open("file", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    for i in range(len(tasks)):
        tasks[i] = tasks[i][:-1]

    return tasks
  
def write_tasks(tasks):
    with open("file", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task+"\n")

def ui():
    tasks = []
    while 1:
        print("1 добавить задачу")
        print("2 Удалить задачу")
        print("3 Изменить задачу")
        print("4 чтение задач из файла")
        print("5 Запис в фаил")
        print("6 Вывод всех задач")
        print("7 Выход")

        a = input('ведите номер команды')
        if a =='1':
            tasks = add_task(tasks)
        elif a =='2':
            tasks = remove_task(tasks)
        elif a =='3':
            tasks = edit_task(tasks)
        elif a =='4':
            tasks = read_tasks()
        elif a =='5':
            write_tasks(tasks)
        elif a == '6':
            print_tasks(tasks)
        elif a =='7':
            quit()
