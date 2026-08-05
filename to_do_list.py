tasks = []
while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete & Remove Task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter Task: ")
        tasks.append({"task": task, "done": False})
        print("Task Added!")
    elif choice == '2':
        if not tasks:
            print("No tasks found.")
        else:
            for i, t in enumerate(tasks, 1):
                status = "✅" if t["done"] else " "
                print(f"{i}. {status}  {t['task']}")            
    elif choice == '3':
        try:
            num = int(input("Enter task number: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1) 
                print(f"Task '{removed['task']}' completed and removed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")        
    elif choice == '4':
        print("Goodbye! 👋")
        break    
    else:
        print("Invalid Option.")