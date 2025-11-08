import todo_functions

task = ["Running" , "Walking" , "Exercising" , "Yoga"]


while True : 
  todo_functions.show_menu()

  choice = input("Enter a choice(1-3) : ")

  if choice == "1":
    todo_functions.add_task(task)

  elif choice == "2":
    todo_functions.view_task(task)

  elif choice == "3":
    print("Goodbye.")
    break

  else :
    print("Invalid choice please enter 1,2 or 3")

          