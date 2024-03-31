def write_tasks(tasks):
    with open("file", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task+"\n")

tasks = ["Убраться", "Помыть пол", "Помыть посуду"]
write_tasks(tasks)