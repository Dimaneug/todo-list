def ui():
    tasks = []
    with open('jyk', 'r') as file:
        tasks = file.readlines()

choice = input('Введите число: ')

    print('1 - прочитать задачи')
    print('2 - удаление задачи')
    print('3 - добавление задачи')
    print('4 - изменение задачи')

    if choice == 1:
        tasks = read_tasks(tasks)
    else choice == 2:
        tasks = remove_tasks(tasks)
    else choice == 3:
        tasks = add_tasks(tasks)
    else choice == 4:
        tasks = edit_tasks(tasks)
