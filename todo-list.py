# task = input("enter task name")

# list= task
# print(list)



# tasks= ""

# while tasks=="" :
#     tasks=input("enter task")
# print(tasks)

# tasks = []

# while True :
#   tasks = input("enter task : ")
#   break

tasks = []

while True:
    print()
    print("1 = add task")
    print("2 = list task")
    print("3 = remove task")
    print("4 = quit")

    choice = input("choose (1-4): ").strip()

    if choice == "1":
        text = input("task to add: ").strip()
        if text:
            tasks.append(text)
            print("added:", text)
        else:
            print("please enter a non-empty task.")

    elif choice == "2":
        if not tasks:
            print("list empty — add a task first.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"  {i}. {task}")


    elif choice == "3":
        if not tasks:
            print("nothing to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"  {i}. {task}")
            raw = input("number to remove: ").strip()
            try:
                n = int(raw)
            except ValueError:
                print("that's not a whole number.")
            else:
                if 1 <= n <= len(tasks):
                    removed = tasks.pop(n - 1)
                    print("removed:", removed)
                else:
                    print("number out of range.")

    elif choice == "4":
        print("bye")
        break

    else:
        print("invalid choice — pick 1, 2, 3, or 4.")
