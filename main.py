def read_tasks():
    tasks = []
    with open("file", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    for i in range(len(tasks)):
        tasks[i] = tasks[i][:-1]

    return tasks

print(read_tasks())