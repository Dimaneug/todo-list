def remove_tasks(tasks: list):
    
    list_save = tasks.copy()

    while 1:
        print_tasks(tasks)
        choice = input("какую убрать милорд")
        n=int(choice)
        tasks.pop(choice)
        pot=input("потвердите удаление задачи,1-удалить,2-отмена,3-цикл")
        print (pot)
        a=int(input())
        if a == 1:
            break
        if a== 2:   
            tasks = list_save.copy() 
            break
        if a==3:
            continue
    return tasks
   
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
            add_task()
        elif a =='2':
            remove_task()
        elif a =='3':
            edit_task()
        elif a =='4':
            read_tasks()
        elif a =='5':
            write_tasks(tasks)
        elif a == '6':
            print_tasks(tasks)
        elif a =='7':
            quit()
