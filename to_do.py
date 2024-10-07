def todo():
    tasks = []

    while True:
        print("\n ******** TO - DO LIST ********")
        print("1. Add Task.")
        print("2. See task.")
        print("3. Mark Task as done.")
        print("4. Exit")

        choice = int(input("Entre your choice: "))

        if choice == 1:
            n_task = int(input("How many task you want to add: "))
            for i in range(n_task):
                task = input("Entre you task: ")
                tasks.append({"task": task, "done":False})
                print("task added")


        if choice == 2:
            print("\n tasks")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "not done"
                print(f"{index + 1}. {task['task']} - {status}")

        if choice == 3:
            task_index = int(input("which task you want to mark as done: "))
            if 0 <= task_index <=len(tasks):
                tasks[task_index - 1]["done"] = True
                print("task marked as done")
            else:
                print("invalid task number")

        if choice == 4:
            break

todo()
