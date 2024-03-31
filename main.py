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
   
def print_tasks():
    pass

remove_tasks(["1","2","3"])









