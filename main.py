def remove_tasks(tasks: list):
    print_tasks(tasks)
    list=[]
    


    choice = input("какую убрать милорд")
    n=int(choice)
    tasks.pop(choice)
    list_save = list
    pot=input("потвердите удаление задачи,1-удалить,2-отмена")
    print (pot)
    a=int(input())
    if a == 1:
        tasks.pop(input())
    else:
        list == list_save 

   
def print_tasks():
    pass

remove_tasks(["1","2","3"])









