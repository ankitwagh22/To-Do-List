# To-Do List application

print('-----------------------')
print('*** TO DO LIST ****')
print('-----------------------')

task_list = []

while True:
    print()
    print("1. Add Task")
    print("2. Update Task")
    print("3. Show All Tasks")
    print("4. Close Application")
    print('-----------------------')
    opt = int(input("Enter Choice :"))
    match (opt):
        case 1:
            task = input("Enter Task :")
            task_list.append(task)
            print("Task Added successfully ..!")
        case 2:
            if len(task_list) != 0:
                num_list = []
                for i in range(1,len(task_list)+1):
                    num_list.append(i)
                n = int(input("Enter Task number :"))
                if n in num_list:
                    for i in range(1,len(task_list)+1):
                        if n == i:
                            task = input("Enter Task :")
                            task_list[n-1] = task
                            print("Taks Updated Successfully ...!")
                else:
                    print("Invalid Task Number ..!")
            else:
                print("List is Empty ...!")
        case 3:
            if len(task_list) == 0:
                print("List is Empty ..!")
            else:
                print("****** Task-List **********")
                for i in range(len(task_list)):
                    print(f"{i+1} --> {task_list[i]}")
                print('-----------------------')
        case 4:
            break
        case _:   # default case
            print("Invalid choice ..!")

print('---------------------------')