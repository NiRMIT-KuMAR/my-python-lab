task = ["Running" , "Walking" , "Exercising" , "Yoga"]

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

while True : 
  show_menu()

  choice = input("Enter a choice(1-3) : ")

  if choice == "1":
    add_task(task)

  elif choice == "2":
    view_task(task)

  elif choice == "3":
    print("Goodbye.")
    break

  else :
    print("Invalid choice please enter 1,2 or 3")

          
