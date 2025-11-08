def show_menu():
  print("1. Add Task ")
  print("2. View Task: ")
  print("3. Exit :")


def add_task(task_list):
  add = input("What do you want to add ?")
  task_list.append(add)
  print("Task added.")


def view_task(task_list):
    print("Your Task :")
    for Vtask in task_list:
      print(f"Task : {Vtask}")
